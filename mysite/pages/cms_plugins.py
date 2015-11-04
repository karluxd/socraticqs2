import re

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from pages.models import (
    LandingPlugin,
    BannerPlugin,
    ActiveLearningRatesPlugin,
    ListPlugin,
    ChildPersonalGuidesPlugin,
    ParentPersonalGuidesPlugin,
    WorkshopDescriptionPlugin
)


class LandingPagePlugin(CMSPluginBase):
    model = LandingPlugin
    render_template = "pages/landing_plugin.html"


class BannerPagePlugin(CMSPluginBase):
    model = BannerPlugin
    render_template = "pages/banner_plugin.html"


class ActiveLearningRatesPagePlugin(CMSPluginBase):
    model = ActiveLearningRatesPlugin
    render_template = 'pages/active_learning_rates_plugin.html'


class ListPagePlugin(CMSPluginBase):
    model = ListPlugin
    render_template = 'pages/list_plugin.html'

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
            'list_text': re.findall(r'<li>.+</li>', instance.list_text),
        })
        return context


class ChildPersonalGuidesPagePlugin(CMSPluginBase):
    render_template = 'pages/personal_guides_child.html'
    name = 'Personal_Guides_Child'
    model = ChildPersonalGuidesPlugin
    require_parent = True
    parent_classes = ['ParentPersonalGuidesPagePlugin']


class ParentPersonalGuidesPagePlugin(CMSPluginBase):
    render_template = 'pages/personal_guides_parent.html'
    name = 'Personal_Guides_Parent'
    model = ParentPersonalGuidesPlugin
    allow_children = True
    require_parent = True
    child_classes = ['ChildPersonalGuidesPagePlugin']
    parent_classes = ['WorkshopDescriptionPagePlugin']


class WorkshopDescriptionPagePlugin(CMSPluginBase):
    render_template = 'pages/workshop_description_plugin.html'
    name = 'Workshop Description Base Plugin'
    model = WorkshopDescriptionPlugin
    allow_children = True
    child_classes = ['ParentPersonalGuidesPagePlugin']


plugin_pool.register_plugin(BannerPagePlugin)
plugin_pool.register_plugin(LandingPagePlugin)
plugin_pool.register_plugin(ActiveLearningRatesPagePlugin)
plugin_pool.register_plugin(ListPagePlugin)
plugin_pool.register_plugin(ParentPersonalGuidesPagePlugin)
plugin_pool.register_plugin(ChildPersonalGuidesPagePlugin)
plugin_pool.register_plugin(WorkshopDescriptionPagePlugin)
