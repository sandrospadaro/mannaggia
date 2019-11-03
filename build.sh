#!/bin/bash
mkdir mannaggia-${MANNAGGIA_VERS} && \
    cp configure mannaggia-${MANNAGGIA_VERS}/ && \
    cp -r src mannaggia-${MANNAGGIA_VERS}/mannaggia-${MANNAGGIA_VERS} && \
    tar cvfz mannaggia-${MANNAGGIA_VERS}.tar.gz mannaggia-${MANNAGGIA_VERS} && \
    cp mannaggia.spec ~/rpmbuild/SPECS/ && \
    cp mannaggia-${MANNAGGIA_VERS}.tar.gz ~/rpmbuild/SOURCES/ && \
    rpmbuild -ba ~/rpmbuild/SPECS/mannaggia.spec && \
    cp ~/rpmbuild/RPMS/noarch/mannaggia-${MANNAGGIA_VERS}-1.noarch.rpm bin/noarch/