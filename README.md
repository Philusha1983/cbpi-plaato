# Plaato Devices Plugin for Craftbeerpi3

## Installation

1. Install the plugin via the Add-On menu
2. Reboot Cbpi

## Configuration

This is a sensor plugin so when you go to add a new sensor there will be a new sensor type called Plaato Keg Sensor

There a 3 options to set for this sensor

1. Api Key
   - This is the key you can get by emailing support@plaato.io, you will get one api key per plaato (so this makes it more of an id)
2. Pin
   - This is the metric that you would like to show for the sensor, there are multiple options and they can be found by visiting [Plaato](https://www.plaato.io/api "Plaato")

**Plaato Airlock**

  --------- ------------------- ---------------------------------------------------------- ---------------- -----------------------
  **Pin**   **Name**            **Description**                                            **Value type**   **Example value**

  v102      bpm                 Bubbles per minute\                                        Number           42
                                                                                                            

  v103      temperature         Ambient temperature\                                       String           "22.144149780273438"\
                                                                                                            

  v104      volume              Batch volume\                                              String\          "24.0"\
                                                                                                            

  v105      original gravity    Original gravity of batch. In Oechsle [g/cm3]\             String\          "1.04"\
                                                                                                            

  v106      specific gravity    Estimated specific gravity of batch. In Oechsle [g/cm3]\   String\          "1.0199115"\
                                                                                                            

  v107      abv                 Alcohol by volume in percent [%]\                          String\          "2.6709838"
                                                                                                            

  v108      temperature\_unit   Temperature unit. Either °C or °F\                         String\          "°C"
                                                                                                            

  v109      volume\_unit        Volume unit. Either L or gal\                              String\          "L"
                                                                                                            

  v110      bubbles             Total number of bubbles counted for the current batch\     String\            "170752"
                                                                                                            

  v119      co2                  The total volume of evolved CO2 for the current batch.    String            "113.52909851074219"
  --------- ------------------- ---------------------------------------------------------- ---------------- -----------------------

 

**Plaato Keg**

  --------- ------------------------- --------------------------------------------------------------------- ---------------- -------------------------------
  **Pin**   **Name**                  **Description**                                                       **Value type**   **Example value**

  v47       Pour                      Last pour volume                                                      String           "0.79oz"

  v48       % Beer left               Percent of beer left                                                  Number           12.00

  v49       Pouring                   Tells you if there is pouring                                         String           "0" or "255"

  v51       Amount left               Returns the amount of beer left based on the unit chosen              String           "12.40"

  v56       Raw temperature           The raw temperature of the device                                     String           "30.125"

  v59       Last pour                 The last pour read by the Plaato keg                                  String           "0.784"

  v62       Empty keg weight          Return the empty keg weight                                           String           "4.500"

  v64       Beer Style                Returns the name of the beer given in the app                         String           "Stout"

  v65       Original Gravity          Return the OG set in the app                                          String           "1062"

  v66       Final Gravity             Returns the FG set in the app                                         String           "1010"

  v67       Keg Date                  Returns the keg date set in the app                                   String           "10/09/19"

  v68       ABV%                      Returns the ABV%                                                      String           "5.644"

  v69       Temperature with unit     Returns the temperature with unit                                     String           "30.37°C"

  v71       Unit type                 Returns a number for the chosen unit type                             String           "1" Metric, "2" US \
                                                                                                                             

  v73       Mass Unit                 Returns the mass unit based on the chosen unit type                   String           "lbs"

  v74       Beer left Unit            Returns the unit based on the chosen unit type and measurement unit   String           "kg"

  v75       Measure Unit              Returns a number for the chosen measurement type                      String           "1" Weight, "2" Volume

  v76       Max Keg Volume            Returns the max keg volume                                            String           "20.000"

  v81       WiFi Strength             Return the WiFi Strength                                              String           "94"

  v82       Volume Unit               Returns the volume unit based on the chosen unit type                 String           "litre"

  v83       Leak detection             Returns 0 if leak not detected and 1 if leak detected                String           "1"

  v86       Min temperature            Returns the minimum temperature set in the app                       String           "-10"

  v87       Max temperature           Returns the maximum tempature set in the app                          String           "35"

  v88       Beer/Co2 Mode             Returns a number based on the mode the app is in                      String           "1" Beer, "2" Co2

  v89       Scale sensitivity         Returns a number based on the scale sensitivity                       String           "1" Low, "2" Medium, "3" High

  v92       Device Core Temperature   Returns the core temperature of the device                            String           "59.44°C"

  v93       Firmware version          Returns the firmware version of the device                            String           "2.0.8"
  --------- ------------------------- --------------------------------------------------------------------- ---------------- -------------------------------



3. Refresh Time
   - This is the interval in which the sensor will call for data from the plaato servers
