import numpy as np
import math #needed for definition of pi

import plotly.graph_objects as go

xpoints=np.arange(0, math.pi*2, 0.05)
ypoints=np.sin(xpoints)

trace0 = go.Scatter(
   x = xpoints, y = ypoints
)
data = [trace0]