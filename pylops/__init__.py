from .LinearOperator import LinearOperator
from .basicoperators import Regression
from .basicoperators import LinearRegression
from .basicoperators import MatrixMult
from .basicoperators import Identity
from .basicoperators import Zero
from .basicoperators import Diagonal
from .basicoperators import Flip
from .basicoperators import Symmetrize
from .basicoperators import Spread
from .basicoperators import Transpose
from .basicoperators import Roll
from .basicoperators import Pad
from .basicoperators import FunctionOperator

from .basicoperators import VStack
from .basicoperators import HStack
from .basicoperators import Block
from .basicoperators import BlockDiag
from .basicoperators import Kronecker

from .basicoperators import CausalIntegration
from .basicoperators import FirstDerivative
from .basicoperators import SecondDerivative
from .basicoperators import Laplacian
from .basicoperators import Gradient
from .basicoperators import Restriction
from .basicoperators import Smoothing1D
from .basicoperators import Smoothing2D

from .avo.poststack import PoststackLinearModelling
from .avo.prestack import PrestackWaveletModelling, PrestackLinearModelling

from .optimization.leastsquares import NormalEquationsInversion, RegularizedInversion
from .optimization.leastsquares import PreconditionedInversion
from .optimization.sparsity import IRLS, ISTA, FISTA, SPGL1, SplitBregman

from .utils.seismicevents import makeaxis, linear2d, parabolic2d
from .utils.tapers import hanningtaper, cosinetaper, taper2d, taper3d
from .utils.wavelets import ricker, gaussian

from . import avo
from . import basicoperators
from . import optimization
from . import signalprocessing
from . import utils
from . import waveeqprocessing

try:
    from .version import version as __version__
except ImportError:
    __version__ = '0.0.0'