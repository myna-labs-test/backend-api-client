"""empty message

Revision ID: 2fc6d90df54d
Revises: beb11a35dbfd
Create Date: 2023-01-17 14:04:01.294117

"""
from alembic import op
import sqlalchemy as sa
from models.characters import Characters, CharacterTextDriver, CharacterTTSDriver


# revision identifiers, used by Alembic.
revision = '2fc6d90df54d'
down_revision = 'beb11a35dbfd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(op.f('uq__characters__id'), 'characters', ['id'])
    op.create_unique_constraint(op.f('uq__messages__id'), 'messages', ['id'])
    bind = op.get_bind()
    session = sa.orm.Session(bind=bind)
    query = sa.insert(Characters).values(
        is_active=True,
        name='Sber chat bot',
        text_driver=CharacterTextDriver.SBER_GPT,
        tts_driver=CharacterTTSDriver.GOOGLE_TTS,
        model_id='sberbank-ai/rugpt3small_based_on_gpt2'
    )
    session.execute(query)
    session.commit()
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('uq__messages__id'), 'messages', type_='unique')
    op.drop_constraint(op.f('uq__characters__id'), 'characters', type_='unique')
    # ### end Alembic commands ###