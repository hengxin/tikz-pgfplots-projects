# tikz-nef
The *nef* TikZ library provides predefined styles and shapes to create diagrams
 for neural networks constructed with the methods of the Neural Engineering
 Framework (NEF) [1].

![Gated difference integrator example.](https://raw.githubusercontent.com/jgosmann/tikz-nef/master/example-net.png)

The example above was generated with this code:

```latex
\begin{tikzpicture}[nef]
    \graph {
        input [ext] -> gate [ens] -> integrator/$x$ [ens] -> output [ext];
        integrator -> [bend right, "$-1$"] gate;
        integrator -> [recurrent] integrator;
        store -> [inhibit] gate;
    };
\end{tikzpicture}
```

The following styles are supported:

* ea: ensemble array
* ens: ensemble
* ext: external input or output
* inhibt: inhibitory connection
* net: network
* pnode: pass-through node
* rect: rectification ensemble
* recurrent: recurrent connection

## Installation

While this package is not available in [CTAN](https://ctan.org/) follow these
instruction:

1. Create the required installation directory (if not already existing):
   `mkdir -p "$(kpsewhich -var-value TEXMFHOME)/tex/generic"`
2. `cd "$(kpsewhich -var-value TEXMFHOME)/tex/generic"`
3. `git clone https://github.com/jgosmann/tikz-nef.git`

## References

[1]: Chris Eliasmith and Charles H. Anderson. Neural engineering: Computation,
     representation, and dynamics in neurobiological systems. MIT Press,
     Cambridge, MA, 2003.
