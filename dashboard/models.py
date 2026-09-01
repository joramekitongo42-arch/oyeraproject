from django.db import models

# The dashboard app has no models of its own. It reads and aggregates
# data from services.models (ServiceRecord, WheelService, PartSale) and
# accounts.models (Customer). "Add new service/wheel job" actions are
# handled by the services app's own create views.
