
Since it's Ubuntu 12.04, I am bundling the app here.

This app uses Ray, which is packaged in Ubuntu. It also needs Open-MPI.

https://launchpad.net/ubuntu/+source/ray
https://launchpad.net/ubuntu/+source/openmpi

Versions:

https://launchpad.net/ubuntu/+source/ray/2.1.0-1
https://launchpad.net/ubuntu/+source/openmpi/1.4.5-1ubuntu1


##############

Versions in DNANexus:

Version 2.2.0-2
Handle: app-

Version 2.2.0-1
Handle: app-B6gpGX0YKz4KVjKpk1p0007v

Version: 2.1.0-1
Handle: app-B6gkJ0Z85Bb2q5YypJp0010j

* Initial version

##############

Testing the app

dx run app-B6gvJkV2kfb7Byjxk55Q010K --input-json-file test/input.json --yes --watch --name "Test Ray 4"
