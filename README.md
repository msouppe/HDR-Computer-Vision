# HDR - High Dynamic Ranging

## Prerequisites
- Python 3 
- Python packages: OpenCV, numpy, matplotlib.pyplot, scipy
- MAC OS or Windows 10 (Ubuntu Windows' Bash)

## Installation 
* Clone the repo:
``` 
git clone https://github.com/msouppe/HDR-Computer-Vision.git
```

* Navigate to `main.py`

* Run the program:
```bash
python3 main.py 
```
  
## Output
**Part 1**  
For every color channel; blue, green, and red, we plot the graphs for the following:  
* Exposure Time vs Brightness  
* Log of Exposure Time vs Log of Brightness with Regression  
* Exposure Time vs Brightness'G  
  
**Part 2**  
For every color channel; blue, green, and red, we plot the graphs for the following:     
* Histogram B'g (a0 * T)   
* Histogram B'g (a1 * T)   
* Histogram B'g (a2 * T)     
* Histogram B'g (a1 * T) / a1      
* Histogram B'g (a2 * T) / a2     
  
**Part 3**  
For every color channel; blue, green, and red, we plot the graphs the composite images for two different algorithms:
* HDR1 Histogram
  * Algorithm 1: Takes the best non-saturated pixels
* HDR2 Histogram 
  * Algorithm 2: Takes the average non-saturated pixels per color channel across the three images

**Part 4** 
Tone-mapped composite HDR final image
* HDR1 image using algorithm 1
* HDR2 image using algorithm 2
