#
# Simple ODE Model
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals
import pybamm


class SimpleODEModel(pybamm.BaseModel):
    """A model consisting of only ODEs.
    Useful for testing solution when variables have domain '[]', and for testing
    broadcasting.

    **Extends**: :class:`pybamm.BaseModel`

    """

    def __init__(self):
        super().__init__()
        whole_cell = ["negative electrode", "separator", "positive electrode"]
        # Create variables: domain is explicitly empty since these variables are only
        # functions of time
        a = pybamm.Variable("a", domain=[])
        b = pybamm.Variable("b", domain=[])
        c = pybamm.Variable("c", domain=[])

        # Simple ODEs
        self.rhs = {a: pybamm.Scalar(2), b: pybamm.Scalar(0), c: -c}

        # Simple initial conditions
        self.initial_conditions = {
            a: pybamm.Scalar(0),
            b: pybamm.Scalar(1),
            c: pybamm.Scalar(1),
        }
        # no boundary conditions for an ODE model
        # Broadcast some of the variables
        self.variables = {
            "a": a,
            "b broadcasted": pybamm.Broadcast(b, whole_cell),
            "c broadcasted": pybamm.Broadcast(c, ["negative electrode", "separator"]),
        }