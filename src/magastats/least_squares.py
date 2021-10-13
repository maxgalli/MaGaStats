import numpy as np
from numpy.linalg import inv
from dataclasses import dataclass
from iminuit import Minuit
from scipy.optimize import minimize
from types import FunctionType
import inspect


@dataclass
class LeastSquares:
    x: np.ndarray
    y: np.ndarray
    model: FunctionType
    covariance: np.ndarray

    def __post_init__(self):
        def to_minimize(params):
            """
            params is an array where the values of the variables are passed in order.
            kwargs is not supported because this signature is the only one which works for both
            minuit and scipy
            """
            model_y = self.model(self.x, *params)
            residuals = self.y - model_y
            return residuals.dot(inv(self.covariance)).dot(residuals)

        self.parameters = tuple(inspect.signature(self.model).parameters.keys())[1:]
        self.to_minimize = to_minimize

    def minimize_with_minuit(self, *args, **kwargs):
        if args:
            m = Minuit(self.to_minimize, args)
        elif kwargs:
            m = Minuit(self.to_minimize, tuple(kwargs[k] for k in self.parameters))
        else:
            raise ValueError()
        m.migrad()
        m.hesse()
        return m

    def minimize_with_scipy(self, *args, **kwargs):
        if args:
            return minimize(self.to_minimize, x0=args, method="Powell")
        elif kwargs:
            return minimize(
                self.to_minimize,
                x0=[kwargs[k] for k in self.parameters],
                method="Powell",
            )
        else:
            raise ValueError()
