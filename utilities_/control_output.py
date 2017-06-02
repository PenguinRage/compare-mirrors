#!/usr/bin/env python

#
# Coded by Joshua Strot
#
# E-Mail: joshuastrot@gmail.com
# URL: https://github.com/joshuastrot/compare-mirrors
#

def output(outFormat, configuration, versionDifferences):
    """
    Output the version differences. 
    """
    
    #Output format done here:
    if not outFormat:
        print("=> Version Changes")
    
        #Output all the versions in plain format
        for repository in configuration["Repositories"]:
            print("    => [" + repository + "] Version Changes")
            for packageName, packageVersions in versionDifferences[repository].items():
                print("        => %s-%s  ->  %s-%s" % (packageName, packageVersions[0], packageName, packageVersions[1]))
    elif outFormat == "yaml":
        # Yaml format:
        #Repository
        #    - Package name
        #        -Manjaro Version
        #        -Arch Version
        print("""# Output generated by compare-mirrors
# 
# Author: Joshua Strot
# URL: https://github.com/joshuastrot/compare-mirrors

        """)
        
        #Output in YAML format
        for repository in configuration["Repositories"]:
            print("\"" + repository + "\":")
            for packageName, packageVersions in versionDifferences[repository].items():
                print("    - \"" + packageName + "\":")
                print("        - \"" + packageVersions[0] + "\"")
                print("        - \"" + packageVersions[1] + "\"")
                
    elif outFormat == "csv":
        # CSV Format:
        #Package Name, Repository, Version One, Version Two
        
        #Output CSV titles
        print("\"Package Name\", \"Repository\", \"Manjaro Version\", \"Arch Version\"")
        
        #Output in YAML format
        for repository in configuration["Repositories"]:
            for packageName, packageVersions in versionDifferences[repository].items():
                print("\"%s\", \"%s\", \"%s\", \"%s\"" % (packageName, repository, packageVersions[0], packageVersions[1]))
                
                
                
                
