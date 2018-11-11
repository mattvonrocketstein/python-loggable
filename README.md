<table>
  <tr><th><strong>python-loggable</strong></th>
    <th style="padding:0px 5px;text-align:right;float:right;">
      <small><small>
      <a href=#overview>Overview</a> |
      <a href=#overview>Design</a> |
      <a href=#prerequisites>Prerequisites</a> |
      <a href=#usage>Usage</a>
      </small><small>
    </th>
  </tr>
  <tr>
    <td width=15%><img src=img/icon.png style="width:150px"></td>
    <td>
    Logging mixins and helpers
    </td>
  </tr>
</table>

## Overview

Placeholder

## Design

Placeholder

## Usage

```
from loggable import get_logger, Loggable

# module-global logger
LOGGER = get_logger(__name__)
LOGGER.debug("hello world")

# the logging mixin
class HelloWorld(Loggable):
  def __init__(self, *args, **kargs):
    super(HelloWorld,self).__init__(*args, **kargs)
    self.debug("hello world")
```
