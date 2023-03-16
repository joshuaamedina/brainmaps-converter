Allow over-ride
if [ -z "${CONTAINER_IMAGE}" ]
then
    version=$(cat ./_util/VERSION)
    CONTAINER_IMAGE="index.docker.io/library/ubuntu:bionic"
fi
. lib/container_exec.sh

BINDPATH=" --bind /opt/intel:/opt/intel "

module unload xalt

mv ${mnifile} userinput.txt

singularity pull brainmap_converter.sif docker://joshuaamedina2000/brainmaps_converter:0.0.1

singularity exec ${BINDPATH} brainmap_converter.sif python3 pythonwrapper.py -t ${source} -c ${conversion}
