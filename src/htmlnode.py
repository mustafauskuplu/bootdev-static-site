import functools

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props or not isinstance(self.props, dict):
            return ""
        
        props_list = list(self.props.items())
        stringified_props_list = map(lambda x: f' {x[0]}="{x[1]}"', props_list)
        return functools.reduce(lambda x, y: f"{x}{y}", stringified_props_list)
    
    def __repr__(self):
        return f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})"