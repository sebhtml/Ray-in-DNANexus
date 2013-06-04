#!/bin/bash

main() {

	echo "Hello"

	numberOfProcessors=$(grep "model name" /proc/cpuinfo | wc -l)
	kmerLength=31
	file1=file1.fastq.gz
	file2=file2.fastq.gz
	output=ray-job
	log=ray.log

	mpiexec -n $numberOfProcessors \
	Ray -k $kmerLength \
	-p $file1 $file2 \
	-o $output \
	&> $log
}

big() {
	main
}
