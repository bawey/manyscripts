#!/bin/bash

SRC_DIR="~/Forge/cmsicms_git-svn/iCMS/src/"
DST_HOST="icmsbox"


if [ -z $1 ]; then
    echo "No source directory given, assuming ${SRC_DIR}"
else
    DST_DIR=$1
    echo "Input directory is ${SRC_DIR}"
fi;

if [ -z $2 ]; then
    echo "No destination host provided, using ${DST_HOST}"
else
   DST_HOST=$2
   echo "Provided ${DST_HOST} as destination"
fi


# eval "scp ${SRC_DIR}/jsp/analysis/admin/*paper* ${DST_HOST}:/opt/Packages/tomcat-portal/webapps/iCMS/jsp/analysis/admin/"

eval "scp ${SRC_DIR}/jsp/analysis/admin/papermanagement.jsp ${DST_HOST}:/opt/Packages/tomcat-portal/webapps/iCMS/jsp/analysis/admin/papermanagement.jsp"
eval "scp ${SRC_DIR}/jsp/analysis/admin/paperaddexternal.jsp ${DST_HOST}:/opt/Packages/tomcat-portal/webapps/iCMS/jsp/analysis/admin/paperaddexternal.jsp"


