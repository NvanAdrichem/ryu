# Copyright (C) 2019 Delft University of Technology, TNO, Niels van Adrichem.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ryu import cfg

CONF = cfg.CONF
CONF.register_cli_opts([
    cfg.BoolOpt('broadcast-to-localport', default=False,
                help='Add local port as output to flood rules, this is among other convenient when running Open vSwitch as softswitch on physical servers and you wish to use the local port to connect to the kernel because the local port is not automatically iterated through.'),
    cfg.BoolOpt('match-on-inport', default=False,
                help='Add incoming port to flow match fields, this is among other convenient when a hardware switch its chip has difficulty differentiating between bridges.')
])
