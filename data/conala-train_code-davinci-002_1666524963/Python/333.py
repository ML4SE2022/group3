I have a plot with multiple lines. I want to avoid line color repetition.

I have tried to use the following code:

<code>
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

for i in range(10):
    y = np.random.rand(100)
    plt.plot(x, y)

plt.show()
</code>

But I get the following plot:

I want to avoid line color repetition.

I have tried to use the following code:

<code>
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

for i in range(10):
    y = np.random.rand(100)
    plt.plot(x, y, color=plt.cm.Set1(i))

plt.show()
</code>

But I get the following plot:

I want to avoid line color repetition.

I have tried to use the following code:

<code>
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

for i in range(10):
    y = np.random.rand(100)
    plt.plot(x, y, color=plt.cm.Set1(i/10))

plt.show()
</code>

But I get the following plot:

I want to avoid line color repetition.

I have tried to use the following code:

<code>
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

for i in range(10):
    y = np.random.rand(100)
    plt.plot(x, y, color=plt.cm.Set1(i/10.0))

plt.show()
</code>

But I get the following plot:

I want to avoid line color repetition.