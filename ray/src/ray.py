#!/usr/bin/env python
# ray 2.1.0-1
# Generated by dx-app-wizard.
#
# Basic execution pattern: Your app will run on a single machine from
# beginning to end.
#
# See https://wiki.dnanexus.com/Developer-Portal for documentation and
# tutorials on how to modify this file.
#
# DNAnexus Python Bindings (dxpy) documentation:
#   http://autodoc.dnanexus.com/bindings/python/current/

import os
import dxpy
import subprocess

# \see https://wiki.dnanexus.com/Developer-Tutorials/Quick-Start
# \see http://autodoc.dnanexus.com/bindings/python/current/dxpy_bindings.html?highlight=get_id#dxpy.bindings.DXDataObject.get_id
# \see https://wiki.dnanexus.com/API-Specification-v1.0.0/Files#API-method%3A-%2Ffile-xxxx%2Fdescribe
# \see http://docs.python.org/2/tutorial/inputoutput.html
@dxpy.entry_point('main')
def main(leftFiles, rightFiles, singleFiles=None):

    # The following line(s) initialize your data object inputs on the platform
    # into dxpy.DXDataObject instances that you can start using immediately.

    leftFiles = [dxpy.DXFile(item) for item in leftFiles]
    rightFiles = [dxpy.DXFile(item) for item in rightFiles]

    # The following line(s) download your file inputs to the local file system
    # using variable names for the filenames.

    command = "mpiexec "

    subprocess.call("grep 'model name' /proc/cpuinfo | wc -l > cores")
    processorFile = open("cores")
    numberOfProcessors = int(processorFile.read())
    processorFile.close()

    command += " -n " + str(numberOfProcessors) + " "
    localLeftFiles = []
    localRightFiles = []
    localSingleFiles = []

    for i in range(len(leftFiles)):
        dataObject = leftFiles[i]
	identifier = dataObject.get_id()
	name = dataObject.describe()["name"]
	localFileName = "leftFiles-" + str(i) + name
        dxpy.download_dxfile(identifier, localFileName)
	localLeftFiles.push(localFileName)

    for i in range(len(rightFiles)):
        dataObject = leftFiles[i]
	identifier = dataObject.get_id()
	name = dataObject.describe()["name"]
	localFileName = "rightFiles-" + str(i) + name
        dxpy.download_dxfile(rightFiles[i].get_id(), localFileName)
	localRightFiles.push(localFileName)

    for i in range(len(singleFiles)):
        dataObject = leftFiles[i]
	identifier = dataObject.get_id()
	name = dataObject.describe()["name"]
	localFileName = "singleFiles-" + str(i) + name
        dxpy.download_dxfile(singleFiles[i].get_id(), localFileName)
	localSingleFiles.push(localFileName)

    # Fill in your application code here.

    pairs = len(leftFiles)
    if len(rightFiles) < pairs:
        pairs = leftFiles

    i = 0
    while i < pairs:
        command += " -p " + localLeftFiles[i] + " " + localRightFiles[i]
        i += 1

    i = 0
    while i < len(localSingleFiles):
        command += " -s " + localSingleFiles[i]
        i += 1

    command += " -o Output "

    subprocess.call(command)

# contigs are in Output/Contigs.fasta
# scaffolds are in Output/Scaffolds.fasta
# distribution is in Output/CoverageDistribution.txt

    # The following line(s) use the Python bindings to upload your file outputs
    # after you have created them on the local file system.  It assumes that you
    # have used the output field name for the filename for each output, but you
    # can change that behavior to suit your needs.

    contigs = dxpy.upload_local_file("contigs");
    scaffolds = dxpy.upload_local_file("scaffolds");
    coverageDistribution = dxpy.upload_local_file("coverageDistribution");

    # The following line fills in some basic dummy output and assumes
    # that you have created variables to represent your output with
    # the same name as your output fields.

    output = {}
    output["contigs"] = dxpy.dxlink(contigs)
    output["scaffolds"] = dxpy.dxlink(scaffolds)
    output["coverageDistribution"] = dxpy.dxlink(coverageDistribution)

    return output

dxpy.run()
