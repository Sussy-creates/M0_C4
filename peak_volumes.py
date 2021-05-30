# M0_C4 - Peak Volumes

def get_peak_volumes(volumes):
    
    peaks = []
    peak  = -73
    for volume in volumes:
        if volume < -72:
            peak = '-Inf'
        elif volume > 10:
            peak = 'CLIP'
        elif peak == 'CLIP' or peak == '-Inf':
            peak = volume
        elif volume > peak:
            peak = volume
        peaks.append(peak)
    return peaks
    return "not implemented"

#### DO NOT TOUCH CODE BELOW THIS LINE ####
if __name__ == '__main__':
    """This code is for manual testing and is provided for your convenience."""
    test_volumes = input("Input space-separated list of volumes: ")
    converted = [int(a) for a in test_volumes.split()]
    print(get_peak_volumes(converted))

