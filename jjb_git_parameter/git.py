import xml.etree.ElementTree as XML

def git_parameter(parser, xml_parent, data):
  """yaml: git

  Example::
    parameters:
      - git:
         name:
         description:
         parameter-type:
         branch:
         branch-filter:
         tag-filter:
         sort-mode:
         default-value:
         quick-filter:
  """
  if data is None:
    data = dict()

  notifier = XML.SubElement(xml_parent, 'net.uaznia.lukanus.hudson.plugins.gitparameter.GitParameterDefinition')
  notifier.set('plugin', 'git-parameter@0.5.1')

  for opt, attr in (
            ('name', 'name'),
            ('description', 'description'),
            ('parameter-type', 'type'),
            ('branch', 'branch'),
            ('branch-filter', 'branchFilter'),
            ('tag-filter', 'tagFilter'),
            ('sort-mode', 'sortMode'),
            ('default-value', 'defaultValue'),
            ('quick-filter', 'quickFilterEnabled')
   ):
     value = data.get(opt, '')
     if isinstance(notifier, str):
       XML.SubElement(data, attr).text = value
     else:
      XML.SubElement(notifier, attr).text = str(value)
