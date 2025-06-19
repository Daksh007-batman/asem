from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    user_type = (
        (1, 'Super_Admin'),
        (2, 'Aviconn_admin'),
        (3, 'Aviconn_Executive'),
        (4, 'Customer'),
        (5, 'Cust_Site_Manager'),
    )
    UserType = models.PositiveIntegerField(default=1, choices=user_type)
    contact_number = models.CharField(max_length=15, help_text='Enter your contact number')

#site model 1NF
class Site(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sites', null=True, blank=True)
    site_name = models.CharField(max_length=25)
    SITE_TYPE = (
        (1, 'Wh_Metering'),
        (2, 'Wh_Energy_Saving'),
        (3, 'Fire_monitoring_system'),
        (4, 'FEMS'),
        (5, 'Wh_submetering'),
    )
    site_type = models.PositiveIntegerField(choices = SITE_TYPE)
    location = models.CharField(max_length=250)

class aisle_blocks(models.Model):
    total_no_of_blocks = models.PositiveIntegerField(null=True, blank=True)
    total_no_of_aisles = models.PositiveIntegerField(null=True, blank=True)
    location = models.CharField(max_length=250, null=True, blank=True)
    
class metersInfo(models.Model):
    per_unit_cost = models.FloatField(null=True, blank=True)
    genset_unit_rate = models.FloatField(null=True, blank=True)
    no_of_single_source_meters = models.PositiveIntegerField(null=True, blank=True)
    no_of_dual_source_meters = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(null=True, blank=True)
    is_visible = models.BooleanField(null=True, blank=True)
    is_live = models.BooleanField(default=False)

class site_data(models.Model):
    live_date = models.DateTimeField(null=True, blank=True)
    baseline_date = models.DateTimeField(null=True, blank=True)
    current_baseline = models.FloatField(null=True, blank=True)
    consumed_energy = models.FloatField(null=True, blank=True)
    total_energy_saved = models.FloatField(null=True, blank=True)

class site_manager_info(models.Model):
    site_manager = models.CharField(max_length=50, null=True, blank=True)
    site_manager_contact = models.CharField(max_length=50, null=True, blank=True)
    site_manager_email = models.EmailField(max_length=50, null=True, blank=True)

class saving(models.Model):
    avg_saving = models.FloatField(null=True, blank=True)
    max_saving = models.FloatField(null=True, blank=True)
    min_saving = models.FloatField(null=True, blank=True)

class Threshold_value(models.Model):
    max_threshold_value = models.FloatField(blank=True, null=True)
    min_threshold_value = models.FloatField(blank=True, null=True)

class is_saving(models.Model):
    is_pf_visible = models.BooleanField(default=False)
    is_loadGraph_visible = models.BooleanField(default=False)

class dg_data(models.Model):
    show_dg_mains_run_time = models.BooleanField(default=False)
    dg_fuel_system_installed = models.BooleanField(default=False)
    partner_dg_fuel_id = models.CharField(max_length=50, null=True, blank=True)

class customer(models.Model):
    customer_visible_dg_fuel_data = models.BooleanField(default=False)
    customer_dg_fuel_visible_date = models.DateTimeField(null=True, blank=True)
    is_hourly_data_visible_customer = models.BooleanField(default=False)

class phaseCurrent(models.Model):
    r_phase_pf_threshold = models.FloatField(default=0, blank=True, null=True)
    y_phase_pf_threshold = models.FloatField(default=0, blank=True, null=True)
    b_phase_pf_threshold = models.FloatField(default=0, blank=True, null=True)

class carbonEmission(models.Model):
    is_carbon_emission_visible = models.BooleanField(default=False)
    carbon_emission_value = models.FloatField(default=0, null=True, blank=True)

class alarms(models.Model):
    is_alarm_History_active = models.BooleanField(default=False)
    show_voltage_alarms = models.BooleanField(default=False)

class VoltageThreshold(models.Model):
    r_phase_voltage_threshold_max = models.FloatField(null=True, blank=True)
    y_phase_voltage_threshold_max = models.FloatField(null=True, blank=True)
    b_phase_voltage_threshold_max = models.FloatField(null=True, blank=True)
    r_phase_voltage_threshold_min = models.FloatField(null=True, blank=True)
    y_phase_voltage_threshold_min = models.FloatField(null=True, blank=True)
    b_phase_voltage_threshold_min = models.FloatField(null=True, blank=True)

class pf_threshold(models.Model):
    r_phase_pf_threshold = models.FloatField(null=True, blank=True)
    y_phase_pf_threshold = models.FloatField(null=True, blank=True)
    b_phase_pf_threshold = models.FloatField(null=True, blank=True)

class dg_info(models.Model):
    dg_fuel_tank_capacity = models.FloatField(null=True, blank=True)
    dg_fuel_minimum_level = models.FloatField(null=True, blank=True)
    dg_overtime = models.FloatField(blank=True, null=True)

#Site class ends here 

# Aisle group 1NF
class AisleGroup(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    attached_leg_id = models.CharField(max_length=30)
    aisleGroupName = models.CharField(max_length=100)

class lights(models.Model):
    total_lights = models.CharField(max_length=10)
    one_light_watt = models.CharField(max_length=30)

class consumption(models.Model):
    expected_consumption = models.FloatField(blank=True, null=True)
    cumulative_consumption = models.FloatField(default=0)

class sensors(models.Model):
    on_sensor_power = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)
    visible_date = models.DateField(blank=True, null=True)

class powersource(models.Model):
    is_this_power_source = models.BooleanField(default=False)
    sources = ((0, "MAINS SUPPLY"), (1, "DG "), (2, "DG 1"), (3, "DG 2"), (4, "DG 3"), (5, "DG 4"))
    power_source = models.PositiveIntegerField(default=0, choices=sources)
    r_phase_pf_threshold = models.FloatField(default=0)
    y_phase_pf_threshold = models.FloatField(default=0)
    b_phase_pf_threshold = models.FloatField(default=0)
    load_graph_color = models.CharField(max_length=30)

# AisleGroup class ends here

class HomeGatewayId(models.Model):
    hgw_id = models.CharField(max_length=200)
    rsssh_port = models.CharField(max_length=50, unique=True)
    monitoring_port = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.hgw_id

