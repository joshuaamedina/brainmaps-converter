import os
import subprocess
import argparse
import logging


logging.basicConfig(level=logging.INFO,
format='%(asctime)s %(levelname)s %(message)s',
      filename='converter.log',
      filemode='w')


parser = argparse.ArgumentParser(description ='vina commands')
parser.add_argument('-t','--template',type=str,required=True,
                    help='Template of MNI or TAL file')
parser.add_argument('-c','--conversion',type=str,required=True,
                    help='Conversion type, MNI to TAL or TAL to MNI')
args = parser.parse_args()


TEMPLATE = args.template
CONVERSION = args.conversion

logging.info(f"TEMPLATE: {TEMPLATE}, CONVERSION: {CONVERSION}")

if CONVERSION == 'MNI2TAL':
    HEADER = '// Reference=Talairach'
    SCRIPTS = {
        "SPM": 'a',
        "FSL": 'b',
        "Other": 'c',
        "AFNI": 'c'
    }
else:
    HEADER = '// Reference=MNI'
    SCRIPTS = {
        "SPM": 'd',
        "FSL": 'e',
        "Other": 'f',
        "AFNI": 'f'
    }

print(TEMPLATE)
print(CONVERSION)
print(SCRIPTS[TEMPLATE])

def main():
    l1 = []
    with open("userinput.txt") as fh:
        for line in fh:
            if line.startswith("//"):
                l1.append(line.replace('\n', ''))

    try:
        os.remove('results.txt')
        os.remove('results.dat')
    except Exception as e:
        print(e)
        logging.info(f"Did not remove results files. Did not exist in user system.")

    # MATLAB COMMAND
    subprocess.run([f"""/scratch/tacc/apps/matlab/2022b/bin/matlab -nodisplay -nosplash -nodesktop -r "wrapper {SCRIPTS[TEMPLATE]}" """],shell=True)


    # Read in the file
    if os.path.isfile('results.dat') == False:
        logging.error(f"ENSURE MATRIX INPUT IS 3 by N OR N by 3")

    with open('results.dat', 'r') as file :
        filedata = file.read()
    
    # Replace the target string
    l2 = filedata.split('NaN')
    l3 = []
    for x in l2:
        if x.isspace():
            continue
        l3.append(x)


    # Write the file out again
    counter = 2
    with open('results.txt', 'w+') as file:
        file.write(HEADER+ '\n')
        file.write(l1[1]+ '\n' + '\n')
        for x in l3:
            file.write(l1[counter] + '\n')
            file.write(l1[counter+1])
            if x[0] != '\n':
                file.write('\n')
            file.write(x + '\n')
            counter += 2
    
    # Clean user output

    os.remove('results.dat')
    os.remove('userinput.txt')


if __name__ == '__main__':
    main()
