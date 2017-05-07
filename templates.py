
PLANET_TEMPLATE = """
Planet    "{name}"
{{
    ParentBody     "{star_name}"
    Class          "Terra"

    Mass            {mass}
    Radius          {radius}

    Color          ({color})

    Orbit
    {{
        RefPlane        "Equator"
        SemiMajorAxis   {semimajoraxis}
        Eccentricity    {eccentricity}
        Inclination     {inclination}
        AscendingNode   {ascending_node}
        MeanAnomaly     {mean_anomaly}
    }}
}}
"""




PLANETE_MODEL = """
Planet    "ES 1"
{
    ParentBody     "EngineeredSystemStar"
    Class          "Terra"

    Mass            0.986073
    Radius          6160.23
    InertiaMoment   0.33103

    Oblateness      0.00143271

    AlbedoBond      0.26
    AlbedoGeom      0.312
    Brightness      2
    Color          (0.612 0.501 0.457)

    Life
    {
        Class   "Organic"
        Type    "Unicellular"
        Biome   "Marine"
    }

    Surface
    {
        SurfStyle       0.885496
        OceanStyle      0.320897
        Randomize      (-0.064, -0.124, 0.979)
        colorDistMagn   0.063709
        colorDistFreq   776.737
        detailScale     15844.4
        colorConversion true
        seaLevel        0.161256
        snowLevel       0.85
        tropicLatitude  0.0881479
        icecapLatitude  0.940951
        icecapHeight    0.163592
        climatePole     0.9375
        climateTropic   0.520814
        climateEquator  0.6875
        heightTempGrad  0.416686
        tropicWidth     0.368556
        mainFreq        0.988187
        venusFreq       1.1938
        venusMagn       0.441174
        mareFreq        6.94499
        mareDensity     0.0630547
        terraceProb     0.175671
        erosion         0.136931
        montesMagn      0.237089
        montesFreq      331.621
        montesSpiky     0.94279
        montesFraction  0.221555
        dunesMagn       0.0585431
        dunesFreq       62.0593
        dunesFraction   0.385597
        hillsMagn       0.138826
        hillsFreq       649.552
        hillsFraction   0.518708
        hills2Fraction  0.910371
        riversMagn      47.4856
        riversFreq      2.29123
        riversSin       4.77895
        riversOctaves   2
        canyonsMagn     0.0469555
        canyonsFreq     172.201
        canyonFraction  0.131002
        cracksMagn      0.127348
        cracksFreq      0.614722
        cracksOctaves   0
        craterMagn      0.567085
        craterFreq      17.8654
        craterDensity   0
        craterOctaves   0
        volcanoMagn     0.680721
        volcanoFreq     0.720443
        volcanoDensity  0.4
        volcanoOctaves  3
        volcanoActivity 1.24213
        volcanoFlows    0.432317
        volcanoRadius   0.454659
        volcanoTemp     1419.26
        lavaCoverTidal  0
        lavaCoverSun    0
        lavaCoverYoung  0
        stripeZones     2.47988
        stripeTwist     0.0976797
        cycloneMagn     2.7776
        cycloneFreq     1.12928
        cycloneDensity  0.380225
        cycloneOctaves  4
        colorSea       (0.040, 0.100, 0.200, 1.000)
        colorShelf     (0.150, 0.480, 0.460, 1.000)
        colorBeach     (0.480, 0.380, 0.280, 0.000)
        colorDesert    (0.410, 0.280, 0.180, 0.000)
        colorLowland   (0.310, 0.230, 0.170, 0.000)
        colorUpland    (0.510, 0.330, 0.190, 0.000)
        colorRock      (0.220, 0.210, 0.210, 0.000)
        colorSnow      (1.000, 1.000, 1.000, 1.308)
        colorLowPlants (0.310, 0.230, 0.170, 0.000)
        colorUpPlants  (0.510, 0.330, 0.190, 0.000)
        BumpHeight      19.4526
        BumpOffset      3.13685
        DiffMapAlpha   "Water"
        SpecBrightWater 0.65
        SpecBrightIce   0.85
        SpecularPower   55
        Hapke           0
        SpotBright      4
        SpotWidth       0.05
        DayAmbient      0.07
    }

    Clouds
    {
        Height          4.03271
        Velocity        98.8254
        BumpHeight      4.03274
        Hapke           0.2
        SpotBright      2
        SpotWidth       0.15
        DayAmbient      2
        mainFreq        1.06099
        mainOctaves     10
        Coverage        0.1
        stripeZones     2.47988
        stripeTwist     0.0976797
    }

    Clouds
    {
        Height          8.06543
        Velocity        127.469
        BumpHeight      4.03274
        Hapke           0.2
        SpotBright      2
        SpotWidth       0.15
        DayAmbient      2
        mainFreq        1.06099
        mainOctaves     10
        Coverage        0.1
        stripeZones     2.47988
        stripeTwist     0.0976797
    }

    Ocean
    {
        Height          3.13685
        Hapke           0
        SpotBright      2
        SpotWidth       0.15
        DayAmbient      2
    }

    NoLava          true

    Atmosphere
    {
        Model          "Neptune"
        Height          46.047
        Density         4.68374
        Pressure        2.60993
        Greenhouse      4.99031
        Bright          10
        Opacity         1
        SkyLight        3.33333
        Hue             -0.0281876
        Saturation      0.940061

        Composition
        {
            CO2       98.7147
            O2        1.03227
            N2        0.224815
            SO2       0.0264266
            H2O       0.000857749
            Ar        0.000304812
            CH4       0.000215742
            C2H2      0.000173959
            H2S       9.43045e-005
            NH3       7.13463e-005
            C2H4      3.90447e-005
            C2H6      1.13298e-005
        }
    }

    Aurora
    {
        Height      54.5323
        NorthLat    56.362
        NorthLon    -16.4434
        NorthRadius 1091.11
        NorthWidth  381.034
        NorthRings  3
        NorthBright 0.3
        NorthParticles 50000
        SouthLat    -73.3731
        SouthLon    163.685
        SouthRadius 1235.53
        SouthWidth  439.876
        SouthRings  2
        SouthBright 0.3
        SouthParticles 50000
        TopColor    (1.000 1.000 1.000)
        BottomColor (0.000 1.000 0.000)
    }

    NoRings         true

    NoAccretionDisk true

    NoCometTail     true

    Orbit
    {
        RefPlane        "Equator"
        SemiMajorAxis   1.0
        Eccentricity    0.0
        Inclination     0.0
        AscendingNode   99.2429
        ArgOfPericenter 229.944
        MeanAnomaly     200.939
    }
}

Planet    "ES 2"
{
    ParentBody     "EngineeredSystemStar"
    Class          "Terra"

    Mass            0.986073
    Radius          6160.23
    InertiaMoment   0.33103

    Oblateness      0.00143271

    AlbedoBond      0.26
    AlbedoGeom      0.312
    Brightness      2
    Color          (0.612 0.501 0.457)

    Life
    {
        Class   "Organic"
        Type    "Unicellular"
        Biome   "Marine"
    }

    Surface
    {
        SurfStyle       0.885496
        OceanStyle      0.320897
        Randomize      (-0.064, -0.124, 0.979)
        colorDistMagn   0.063709
        colorDistFreq   776.737
        detailScale     15844.4
        colorConversion true
        seaLevel        0.161256
        snowLevel       0.85
        tropicLatitude  0.0881479
        icecapLatitude  0.940951
        icecapHeight    0.163592
        climatePole     0.9375
        climateTropic   0.520814
        climateEquator  0.6875
        heightTempGrad  0.416686
        tropicWidth     0.368556
        mainFreq        0.988187
        venusFreq       1.1938
        venusMagn       0.441174
        mareFreq        6.94499
        mareDensity     0.0630547
        terraceProb     0.175671
        erosion         0.136931
        montesMagn      0.237089
        montesFreq      331.621
        montesSpiky     0.94279
        montesFraction  0.221555
        dunesMagn       0.0585431
        dunesFreq       62.0593
        dunesFraction   0.385597
        hillsMagn       0.138826
        hillsFreq       649.552
        hillsFraction   0.518708
        hills2Fraction  0.910371
        riversMagn      47.4856
        riversFreq      2.29123
        riversSin       4.77895
        riversOctaves   2
        canyonsMagn     0.0469555
        canyonsFreq     172.201
        canyonFraction  0.131002
        cracksMagn      0.127348
        cracksFreq      0.614722
        cracksOctaves   0
        craterMagn      0.567085
        craterFreq      17.8654
        craterDensity   0
        craterOctaves   0
        volcanoMagn     0.680721
        volcanoFreq     0.720443
        volcanoDensity  0.4
        volcanoOctaves  3
        volcanoActivity 1.24213
        volcanoFlows    0.432317
        volcanoRadius   0.454659
        volcanoTemp     1419.26
        lavaCoverTidal  0
        lavaCoverSun    0
        lavaCoverYoung  0
        stripeZones     2.47988
        stripeTwist     0.0976797
        cycloneMagn     2.7776
        cycloneFreq     1.12928
        cycloneDensity  0.380225
        cycloneOctaves  4
        colorSea       (0.040, 0.100, 0.200, 1.000)
        colorShelf     (0.150, 0.480, 0.460, 1.000)
        colorBeach     (0.480, 0.380, 0.280, 0.000)
        colorDesert    (0.410, 0.280, 0.180, 0.000)
        colorLowland   (0.310, 0.230, 0.170, 0.000)
        colorUpland    (0.510, 0.330, 0.190, 0.000)
        colorRock      (0.220, 0.210, 0.210, 0.000)
        colorSnow      (1.000, 1.000, 1.000, 1.308)
        colorLowPlants (0.310, 0.230, 0.170, 0.000)
        colorUpPlants  (0.510, 0.330, 0.190, 0.000)
        BumpHeight      19.4526
        BumpOffset      3.13685
        DiffMapAlpha   "Water"
        SpecBrightWater 0.65
        SpecBrightIce   0.85
        SpecularPower   55
        Hapke           0
        SpotBright      4
        SpotWidth       0.05
        DayAmbient      0.07
    }

    Clouds
    {
        Height          4.03271
        Velocity        98.8254
        BumpHeight      4.03274
        Hapke           0.2
        SpotBright      2
        SpotWidth       0.15
        DayAmbient      2
        mainFreq        1.06099
        mainOctaves     10
        Coverage        0.1
        stripeZones     2.47988
        stripeTwist     0.0976797
    }

    Clouds
    {
        Height          8.06543
        Velocity        127.469
        BumpHeight      4.03274
        Hapke           0.2
        SpotBright      2
        SpotWidth       0.15
        DayAmbient      2
        mainFreq        1.06099
        mainOctaves     10
        Coverage        0.1
        stripeZones     2.47988
        stripeTwist     0.0976797
    }

    Ocean
    {
        Height          3.13685
        Hapke           0
        SpotBright      2
        SpotWidth       0.15
        DayAmbient      2
    }

    NoLava          true

    Atmosphere
    {
        Model          "Neptune"
        Height          46.047
        Density         4.68374
        Pressure        2.60993
        Greenhouse      4.99031
        Bright          10
        Opacity         1
        SkyLight        3.33333
        Hue             -0.0281876
        Saturation      0.940061

        Composition
        {
            CO2       98.7147
            O2        1.03227
            N2        0.224815
            SO2       0.0264266
            H2O       0.000857749
            Ar        0.000304812
            CH4       0.000215742
            C2H2      0.000173959
            H2S       9.43045e-005
            NH3       7.13463e-005
            C2H4      3.90447e-005
            C2H6      1.13298e-005
        }
    }

    Aurora
    {
        Height      54.5323
        NorthLat    56.362
        NorthLon    -16.4434
        NorthRadius 1091.11
        NorthWidth  381.034
        NorthRings  3
        NorthBright 0.3
        NorthParticles 50000
        SouthLat    -73.3731
        SouthLon    163.685
        SouthRadius 1235.53
        SouthWidth  439.876
        SouthRings  2
        SouthBright 0.3
        SouthParticles 50000
        TopColor    (1.000 1.000 1.000)
        BottomColor (0.000 1.000 0.000)
    }

    NoRings         true

    NoAccretionDisk true

    NoCometTail     true

    Orbit
    {
        RefPlane        "Equator"
        SemiMajorAxis   1.0
        Eccentricity    0.0
        Inclination     0.0
        AscendingNode   59.2429
        ArgOfPericenter 229.944
        MeanAnomaly     200.939
    }
}
"""
