"""cvss_model

Revision ID: d8f0b32a5c0e
Revises: 89115e133f0a
Create Date: 2021-09-01 10:30:06.693843+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8f0b32a5c0e'
down_revision = '89115e133f0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('impact_type',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=12), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('cvss_base',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('version', sa.String(length=8), nullable=False),
                    sa.Column('vector_string', sa.String(length=64), nullable=False),
                    sa.Column('confidentiality_impact_id', sa.Integer(), nullable=True),
                    sa.Column('integrity_impact_id', sa.Integer(), nullable=True),
                    sa.Column('availability_impact_id', sa.Integer(), nullable=True),
                    sa.Column('type', sa.String(length=24), nullable=True),
                    sa.ForeignKeyConstraint(['availability_impact_id'], ['impact_type.id'], ),
                    sa.ForeignKeyConstraint(['confidentiality_impact_id'], ['impact_type.id'], ),
                    sa.ForeignKeyConstraint(['integrity_impact_id'], ['impact_type.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('cvss_v2',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('access_vector',
                              sa.Enum('Network Adjacent', 'Local', 'Network', name='cvss_access_vector'),
                              nullable=False),
                    sa.Column('access_complexity', sa.Enum('Low', 'Medium', 'High', name='cvss_access_complexity'),
                              nullable=False),
                    sa.Column('authentication', sa.Enum('None', 'Single', 'Multiple', name='cvss_authentication'),
                              nullable=False),
                    sa.ForeignKeyConstraint(['id'], ['cvss_base.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('cvss_v3',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('attack_vector',
                              sa.Enum('Network Adjacent', 'Local', 'Physical', name='cvss_attack_vector'),
                              nullable=False),
                    sa.Column('attack_complexity', sa.Enum('Low', 'High', name='cvss_attack_complexity'),
                              nullable=False),
                    sa.Column('privileges_required', sa.Enum('None', 'Low', 'High', name='cvss_privileges_required'),
                              nullable=False),
                    sa.Column('user_interaction', sa.Enum('None', 'Required', name='cvss_user_interaction'),
                              nullable=False),
                    sa.Column('scope', sa.Enum('None', 'Required', name='cvss_scope'), nullable=False),
                    sa.ForeignKeyConstraint(['id'], ['cvss_base.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )

    # Vuln relationship with cvss
    op.add_column('vulnerability', sa.Column('cvssv2_id', sa.Integer(), nullable=True))
    op.add_column('vulnerability', sa.Column('cvssv3_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'vulnerability', 'cvss_v2', ['cvssv2_id'], ['id'])
    op.create_foreign_key(None, 'vulnerability', 'cvss_v3', ['cvssv3_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.drop_constraint(None, 'vulnerability', type_='foreignkey')
    op.drop_column('vulnerability', 'cvssv2_id')
    op.drop_column('vulnerability', 'cvssv3_id')
    op.drop_table('cvss_v3')
    op.drop_table('cvss_v2')
    op.drop_table('cvss_base')
    op.drop_table('impact_type')
    """
    drop type cvss_attack_complexity
    drop type cvss_access_complexity
    drop type cvss_access_vector;
    drop type cvss_attack_vector;
    drop type cvss_authentication;
    drop type cvss_privileges_required;
    drop type cvss_scope;
    drop type cvss_user_interaction;
    """
    #
    # ### end Alembic commands ###
