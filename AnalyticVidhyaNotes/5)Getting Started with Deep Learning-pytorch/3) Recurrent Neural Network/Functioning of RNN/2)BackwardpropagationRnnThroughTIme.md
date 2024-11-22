Backward Propagation RNN through Time:
======================================

1) calculate Loss( y^ -y)
2) compute the gradients with respect to weights matrices (u,v,w)  du/dt,dv/de,dw/de (d is paratial derivate short d)
3) update weights -> u,v,w using gradients.

Compute Gradients:
==================

1) dL/dv, dL/dw, dL/du

Backward propagation - compute weight:
======================================

dl/dw - how to compute weight

dl/dw = (dl/dy^) .(dy/dh3) .(dh3/dw)

        h3 = g(wh2+vx) // h2 is previous state.
         
