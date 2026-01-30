# rosbag to pandas

Helper functions to extract data from ROS bag files and organize into pandas-compatible structures.

This was almost by Claude...

## Features

- Convert ROS bag files to HDF5 format
- Load HDF5 datasets into pandas DataFrames
- Support for nested ROS message types (Pose, Twist, Vector3, etc.)
- Handle fixed-length and dynamic arrays
- List topics in bag files without reading all messages
- Export to pandas-compatible HDF5 format

## Installation

```bash
pip install rosbag_to_pandas
```

Or install from source:

```bash
git clone https://github.com/yourusername/rosbag_to_pandas.git
cd rosbag_to_pandas
pip install -e .
```

## Quick Start

### Convert a ROS bag to HDF5

```python
from rosbag_to_pandas import bag2hdf5

# Convert entire bag file
bag2hdf5('my_data.bag', 'output.hdf5', max_strlen=255)

# Convert specific topics only
bag2hdf5('my_data.bag', 'output.hdf5', 
         topics=['/mavros/imu/data', '/trisonica'],
         max_strlen=255)
```

### List topics in a bag file

```python
from rosbag_to_pandas import list_bag_topics

# Quick overview of bag contents
topics_info = list_bag_topics('my_data.bag')
```

### Load HDF5 data into pandas

```python
from rosbag_to_pandas import (
    find_all_datasets,
    get_pandas_dataframe_from_uncooperative_hdf5,
    list_hdf5_keys,
    save_all_datasets_to_hdf5
)

# Explore available datasets
datasets = find_all_datasets('output.hdf5')
print(datasets)

# Load a single dataset
df = get_pandas_dataframe_from_uncooperative_hdf5('output.hdf5', key='mavros/imu/data')

# Load multiple datasets
dfs = get_pandas_dataframe_from_uncooperative_hdf5(
    'output.hdf5', 
    key=['mavros/imu/data', 'trisonica']
)

# Load all datasets
all_dfs = get_pandas_dataframe_from_uncooperative_hdf5('output.hdf5', key='all_keys')

# Convert to pandas-friendly HDF5 format
save_all_datasets_to_hdf5('input.hdf5', 'output_pandas.hdf5')
```

### Command Line Usage

```bash
# List topics in a bag file
bag2hdf5 my_data.bag --list-topics

# Convert bag to HDF5
bag2hdf5 my_data.bag --out output.hdf5

# Convert specific topics
bag2hdf5 my_data.bag --topic /mavros/imu/data /trisonica
```

## Package Structure

```
rosbag_to_pandas/
├── rosbag_to_pandas/
│   ├── __init__.py
│   ├── bag2hdf5.py          # Convert ROS bags to HDF5
│   └── load_hdf5.py         # Load HDF5 data into pandas
├── setup.py
├── requirements.txt
├── README.md
└── LICENSE
```

## Supported ROS Message Types

- Standard types: int8, int16, int32, int64, uint8, uint16, uint32, uint64, float32, float64, bool, string
- Time types: time, Header
- Geometry types: Point, Quaternion, Vector3, Pose, Twist, Accel
- Arrays: Both fixed-length (e.g., float64[9]) and dynamic arrays (e.g., float64[])

## Requirements

- Python >= 3.8
- numpy >= 1.19.0
- pandas >= 1.3.0
- h5py >= 3.0.0
- tables >= 3.6.0
- progressbar2 >= 3.50.0
- bagpy >= 0.5.0 (or ROS installation with rosbag)

## Credits

- Original bag2hdf5 script by sdvillal / StrawLab: https://github.com/strawlab/bag2hdf5
- Additional features and pandas integration by Floris van Breugel and Claude

## License

MIT License
