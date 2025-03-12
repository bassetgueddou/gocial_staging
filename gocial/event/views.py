from flask import request, jsonify, render_template, redirect, url_for
from . import event_bp
from app import db
from .models import Event


from .forms import EventForm


@event_bp.route('/', methods=['GET'])
def list_events():
    """Liste tous les événements."""
    events = Event.query.all()

    return render_template('event/list_events.html', events=events)


@event_bp.route('/create', methods=['GET', 'POST'])
def create_event():
    """Créer un nouvel événement."""
    form = EventForm()
    if form.validate_on_submit():
        new_event = Event(
            title=form.title.data,
            description=form.description.data,
            date=form.date.data,
            user_id=1  # TODO: à adapter plutard flemme de récup de la bdd (pgadmine en pls faut régler ça aussi)
        )
        db.session.add(new_event)
        db.session.commit()
        return redirect(url_for('event.list_events'))
    return render_template('event/create_event.html', form=form)


@event_bp.route('/<int:event_id>', methods=['GET'])
def get_event(event_id):
    """Afficher les détails d’un événement."""
    event = Event.query.get_or_404(event_id)

    return render_template('event/detail_event.html', event=event)


@event_bp.route('/<int:event_id>/edit', methods=['GET', 'POST'])
def edit_event(event_id):
    """Modifier un événement existant."""
    event = Event.query.get_or_404(event_id)
    form = EventForm(obj=event)
    if form.validate_on_submit():
        event.title = form.title.data
        event.description = form.description.data
        event.date = form.date.data
        db.session.commit()
        return redirect(url_for('event.get_event', event_id=event.id))
    return render_template('event/edit_event.html', form=form, event=event)


@event_bp.route('/<int:event_id>/delete', methods=['POST'])
def delete_event(event_id):
    """Supprimer un événement."""
    event = Event.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()
    return redirect(url_for('event.list_events'))
