# Fast Algorithm of Multi-source Multi-terminal Network Reliability Assessment

## Preparation

Download the wheel package from the `wheel` folder and install it. A new package named `GraphModule` will be installed.

## Usage

An example is available in `main.py`.

## Requirements

Numpy and NetworkX.

## Test results

The tests were performed under the following environment:

- Language: Python 3.10
- Compiler: MSVC 14.2 (with "-O2")
- Processor: Intel Core i7 12700KF 3.60GHz (12 cores)
- Memory: 64GB RAM


|Name             | number of edges | number of nodes | decomposition time | solution time |
|-----------------|-----------------|-----------------|--------------------|---------------|
|   case5 (Area GK)   |        101      |       88        |        21.42       |      5.89     |
|        case33   |       37        |       33        |        0.51        |      0.18     |

