from enum import Enum


class LinodeInstanceTypes(Enum):
    G6_NANODE_1 = "g6-nanode-1"
    G6_STANDARD_1 = "g6-standard-1"
    G6_STANDARD_2 = "g6-standard-2"
    G6_STANDARD_4 = "g6-standard-4"
    G6_STANDARD_6 = "g6-standard-6"
    G6_STANDARD_8 = "g6-standard-8"
    G6_STANDARD_16 = "g6-standard-16"
    G6_STANDARD_20 = "g6-standard-20"
    G6_STANDARD_24 = "g6-standard-24"
    G6_STANDARD_32 = "g6-standard-32"
    G7_HIGHMEM_1 = "g7-highmem-1"
    G7_HIGHMEM_2 = "g7-highmem-2"
    G7_HIGHMEM_4 = "g7-highmem-4"
    G7_HIGHMEM_8 = "g7-highmem-8"
    G7_HIGHMEM_16 = "g7-highmem-16"
    G6_DEDICATED_2 = "g6-dedicated-2"
    G6_DEDICATED_4 = "g6-dedicated-4"
    G6_DEDICATED_8 = "g6-dedicated-8"
    G6_DEDICATED_16 = "g6-dedicated-16"
    G6_DEDICATED_32 = "g6-dedicated-32"
    G6_DEDICATED_48 = "g6-dedicated-48"
    G6_DEDICATED_50 = "g6-dedicated-50"
    G6_DEDICATED_56 = "g6-dedicated-56"
    G6_DEDICATED_64 = "g6-dedicated-64"
    G1_GPU_RTX6000_1 = "g1-gpu-rtx6000-1"
    G1_GPU_RTX6000_2 = "g1-gpu-rtx6000-2"
    G1_GPU_RTX6000_3 = "g1-gpu-rtx6000-3"
    G1_GPU_RTX6000_4 = "g1-gpu-rtx6000-4"


class LinodeRegions(Enum):
    AP_WEST = "ap-west"
    CA_CENTRAL = "ca-central"
    AP_SOUTHEAST = "ap-southeast"
    US_CENTRAL = "us-central"
    US_WEST = "us-west"
    US_SOUTHEAST = "us-southeast"
    US_EAST = "us-east"
    EU_WEST = "eu-west"
    AP_SOUTH = "ap-south"
    EU_CENTRAL = "eu-central"
    AP_NORTHEAST = "ap-northeast"