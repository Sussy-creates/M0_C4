# M0_C4 - Peak Volumes

def get_peak_volumes(volumes):
    
    output = []
    y = -72
    for x in volumes:
        if x < -72:
            y = '-Inf'
        elif x > 10:
            y = 'CLIP'
        elif y == 'CLIP' or y == '-Inf':
            y = x
        elif x > y:
            y = x
        output.append(y)
    return output
    return "not implemented"

#### DO NOT TOUCH CODE BELOW THIS LINE ####
if __name__ == '__main__':
    """This code is for manual testing and is provided for your convenience."""
    test_volumes = input("Input space-separated list of volumes: ")
    converted = [int(a) for a in test_volumes.split()]
    print(get_peak_volumes(converted))

