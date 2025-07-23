# ExecOrderControllerLite

A lightweight ComfyUI custom node that provides execution order control functionality without the overhead of large dependencies.

## Overview

This custom node is inspired by the [ComfyUI-Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack) by ltdrdata. While Impact-Pack offers many powerful features, sometimes you only need the execution order controller functionality without installing the entire package and its dependencies.

ExecOrderControllerLite extracts just the essential execution order control feature, providing a dependency-free solution for managing node execution flow in your ComfyUI workflows.

## Features

- **Zero Dependencies**: No additional packages or dependencies required
- **Lightweight**: Minimal code footprint
- **Drop-in Replacement**: Compatible interface for execution order control
- **Simple Installation**: Just clone and use

## What is Execution Order Control?

In ComfyUI, nodes execute based on their dependencies. Sometimes you need to ensure certain nodes run in a specific order even when they don't have direct data dependencies. The Execution Order Controller creates an artificial dependency chain by passing through signals and values, forcing downstream nodes to wait for upstream nodes to complete.

## Installation

1. Navigate to your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ExecOrderControllerLite.git
   ```

3. Restart ComfyUI

## Usage

The node appears in the node menu under `Util/Lite` as "Execution Order Controller (Lite)".

### Inputs
- **signal**: Any type - Used to create dependency edges and control execution order
- **value**: Any type - The actual data payload you want to pass through

### Outputs
- **signal**: Returns the input signal unchanged
- **value**: Returns the input value unchanged

### Example Workflow

```
[Node A] → signal → [ExecOrderControllerLite] → signal → [Node C]
           ↓                    ↓
         value  →            value → [Node D]
           ↓
        [Node B]
```

In this setup:
- Node A executes first
- ExecOrderControllerLite waits for Node A to complete
- Nodes C and D wait for ExecOrderControllerLite to complete
- This ensures Node B completes before Nodes C and D execute

## Technical Details

The node uses ComfyUI's `AnyType` system to accept and pass through any data type. It implements a simple passthrough function that returns both inputs unchanged, creating the necessary dependency chain for execution order control.

## Why This Exists

While ComfyUI-Impact-Pack is an excellent package with many features, it comes with substantial dependencies that may not be needed if you only require execution order control. This lightweight alternative:

- Reduces installation complexity
- Minimizes potential conflicts
- Provides faster loading times
- Offers a focused solution for a specific need

## Credits

- Inspired by [ComfyUI-Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack) by ltdrdata
- Built for the ComfyUI community

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Issues

If you encounter any issues or have feature requests, please open an issue on GitHub.

---

**Note**: This is a focused, lightweight implementation. If you need the full feature set of Impact-Pack, consider using the original package instead.
