{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the required initial velocity is  49.04999999999815  m/s\n"
     ]
    }
   ],
   "source": [
    "#throwing a ball vertically\n",
    "\n",
    "from numpy import array\n",
    "from numpy import arange\n",
    "\n",
    "g = 9.81\n",
    "a = 0.0\n",
    "b = 10.0\n",
    "N = 1000\n",
    "h = (b-a)/N\n",
    "target = 1e-10\n",
    "\n",
    "def f(r):\n",
    "    x = r[0]\n",
    "    y = r[1]\n",
    "    fx = y\n",
    "    fy = -g\n",
    "    return array([fx,fy],float)\n",
    "\n",
    "def height(v):\n",
    "    r = array([0.0,v], float)\n",
    "    for t in arange(a,b,h):\n",
    "        k1 = h*f(r)\n",
    "        k2 = h*f(r+0.5*k1)\n",
    "        k3 = h*f(r+0.5*k2)\n",
    "        k4 = h*f(r+k3)\n",
    "        r += (k1+2*k2+2*k3+k4)/6\n",
    "        \n",
    "    return r[0]\n",
    "\n",
    "v1 = 0.01\n",
    "v2 = 1000.0\n",
    "h1 = height(v1)\n",
    "h2 = height(v2)\n",
    "\n",
    "while abs(h2-h1)> target :\n",
    "    vp = (v1+v2)/2\n",
    "    hp = height(vp)\n",
    "    if h1*hp>0:\n",
    "        v1 = vp\n",
    "        h1 = hp\n",
    "    else:\n",
    "        v2 = vp\n",
    "        h2 = hp\n",
    "        \n",
    "v = (v1+v2)/2\n",
    "\n",
    "print(\"the required initial velocity is \" ,v,\" m/s\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
