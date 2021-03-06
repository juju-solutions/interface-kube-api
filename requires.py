#!/usr/bin/python
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from charms.reactive import RelationBase
from charms.reactive import hook
from charms.reactive import scopes


class KubeAPIRequireer(RelationBase):
    scope = scopes.GLOBAL

    @hook('{requires:kube-api}-relation-{joined,changed}')
    def joined_or_changed(self):
        ''' Set the available state if we have the minimum credentials '''
        if self.has_credentials():
            conv = self.conversation()
            conv.set_state('{relation_name}.available')

    def get_data(self):
        ''' Return a small subnet of the data '''
        return {'private-address': self.get_remote('private-address'),
                'port': self.get_remote('port')}

