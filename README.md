# HDR - High Dynamic Ranging

## Prerequisites
- Python 3 
- Python packages: OpenCV, numpy, matplotlib.pyplot, scipy
- MAC OS or Windows 10 (Ubuntu Windows' Bash)

## Installation 
Clone the repo:
``` 
git clone https://github.com/msouppe/HDR-Computer-Vision.git
```

Running the program:
```bash
python3 main.py 
```
  
## Output
*Part 1*  
For every color channel; blue, green, and red, we plot the graphs for the following:  
- Exposure Time vs Brightness  
- Log of Exposure Time vs Log of Brightness with Regression  
- Exposure Time vs Brightness'G  
  
*Part 2*   
For every color channel; blue, green, and red, we plot the graphs for the following:     
- Histogram B'g (a0 * T)   
- Histogram B'g (a1 * T)   
- Histogram B'g (a2 * T)     
- Histogram B'g (a1 * T) / a1      
- Histogram B'g (a2 * T) / a2     
  
*Part 3*

*Part 4*
