from . import __version__ as app_version

app_name = "sebco_customization"
app_title = "Sebco Customization"
app_publisher = "Kipngetich Ngeno"
app_description = "Customization for Sebco Limited"
app_email = "khalifngeno@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sebco_customization/css/sebco_customization.css"
# app_include_js = "/assets/sebco_customization/js/sebco_customization.js"

# include js, css files in header of web template
# web_include_css = "/assets/sebco_customization/css/sebco_customization.css"
# web_include_js = "/assets/sebco_customization/js/sebco_customization.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "sebco_customization/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
	"Budget" : "public/js/budget.js"
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "sebco_customization.utils.jinja_methods",
#	"filters": "sebco_customization.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "sebco_customization.install.before_install"
# after_install = "sebco_customization.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "sebco_customization.uninstall.before_uninstall"
# after_uninstall = "sebco_customization.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sebco_customization.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	# "*": {
	# 	"on_update": "method",
	# 	"on_cancel": "method",
	# 	"on_trash": "method"
	# },
	"Budget": {
        # will run before a Budget record is saved in the database
        "before_save": "sebco_customization.sebco_customization.custom_methods.budget.before_save"
    }
}

# Scheduled Tasks
# ---------------

scheduler_events = {
    "cron": {
		"0/1 * * * *": [
			"sebco_customization.sebco_customization.tasks.test_function"
		],
    },
	# "all": [
	# 	"sebco_customization.tasks.all"
	# ],
	# "daily": [
	# 	"sebco_customization.tasks.daily"
	# ],
	# "hourly": [
	# 	"sebco_customization.tasks.hourly"
	# ],
	# "weekly": [
	# 	"sebco_customization.tasks.weekly"
	# ],
	# "monthly": [
	# 	"sebco_customization.tasks.monthly"
	# ],
}

# Testing
# -------

# before_tests = "sebco_customization.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "sebco_customization.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "sebco_customization.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"sebco_customization.auth.validate"
# ]

fixtures = ["Custom Field"]
