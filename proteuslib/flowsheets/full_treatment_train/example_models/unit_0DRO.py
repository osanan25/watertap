###############################################################################
# ProteusLib Copyright (c) 2021, The Regents of the University of California,
# through Lawrence Berkeley National Laboratory, Oak Ridge National
# Laboratory, National Renewable Energy Laboratory, and National Energy
# Technology Laboratory (subject to receipt of any required approvals from
# the U.S. Dept. of Energy). All rights reserved.
#
# Please see the files COPYRIGHT.md and LICENSE.md for full copyright and license
# information, respectively. These files are also available online at the URL
# "https://github.com/nawi-hub/proteuslib/"
#
###############################################################################

"""0D reverse osmosis examples"""

from pyomo.environ import ConcreteModel
from idaes.core import FlowsheetBlock
from idaes.core.util.scaling import calculate_scaling_factors
from proteuslib.flowsheets.full_treatment_train.example_models import property_models
from proteuslib.unit_models.reverse_osmosis_0D import (ReverseOsmosis0D,
                                                       ConcentrationPolarizationType,
                                                       MassTransferCoefficient,
                                                       PressureChangeType)
from proteuslib.flowsheets.full_treatment_train.util import solve_with_user_scaling, check_dof


def build_RO(m, base='TDS', level='simple', name_str='RO'):
    """
    Builds a 0DRO model at a specified level (simple or detailed).
    Requires prop_TDS property package.
    """
    if base not in ['TDS']:
        raise ValueError('Unexpected property base {base} for build_RO'
                         ''.format(base=base))
    prop = property_models.get_prop(m, base=base)

    if level == 'simple':
        # build unit
        setattr(m.fs, name_str, ReverseOsmosis0D(default={"property_package": prop}))
        blk = getattr(m.fs, name_str)

        # specify unit
        blk.area.fix(50)
        blk.A_comp.fix(4.2e-12)
        blk.B_comp.fix(3.5e-8)
        blk.permeate.pressure[0].fix(101325)

    elif level == 'detailed':
        # build unit
        setattr(m.fs, name_str, ReverseOsmosis0D(default={
            "property_package": prop,
            "has_pressure_change": True,
            "pressure_change_type": PressureChangeType.calculated,
            "mass_transfer_coefficient": MassTransferCoefficient.calculated,
            "concentration_polarization_type": ConcentrationPolarizationType.calculated}))
        blk = getattr(m.fs, name_str)

        # specify unit
        blk.area.fix(50)
        blk.A_comp.fix(4.2e-12)
        blk.B_comp.fix(3.5e-8)
        blk.permeate.pressure[0].fix(101325)
        blk.channel_height.fix(1e-3)
        blk.spacer_porosity.fix(0.97)
        blk.N_Re_io[0, 'in'].fix(500)

    else:
        raise ValueError('Unexpected argument {level} for level in build_RO'
                         ''.format(level=level))

    # scale unit
    calculate_scaling_factors(blk)


def solve_build_RO(base='TDS', level='simple'):
    m = ConcreteModel()
    m.fs = FlowsheetBlock(default={"dynamic": False})
    property_models.build_prop(m, base='TDS')

    build_RO(m, base=base, level=level)

    # specify feed
    property_models.specify_feed(m.fs.RO.feed_side.properties_in[0], base='TDS')
    m.fs.RO.feed_side.properties_in[0].pressure.fix(50e5)

    # initialize
    m.fs.RO.initialize(optarg={'nlp_scaling_method': 'user-scaling'})

    check_dof(m)
    solve_with_user_scaling(m)

    m.fs.RO.report()

    return m


if __name__ == "__main__":
    solve_build_RO(base='TDS', level='simple')
    solve_build_RO(base='TDS', level='detailed')
