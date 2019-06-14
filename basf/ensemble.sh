#!/bin/bash

sgdml all ethanol_T300_resutls_h5.npz 1000 200 1000 --gdml --no_E -o
mv ethanol_T300_resutls_h5-unknown-train1000-sym1.npz ensemble_models/a1.npz

sgdml all ethanol_T300_resutls_h5.npz 200 200 1000 --gdml --no_E -o
mv ethanol_T300_resutls_h5-unknown-train1000-sym1.npz ensemble_models/a2.npz

sgdml all ethanol_T300_resutls_h5.npz 1000 200 1000 --gdml --no_E -o
mv ethanol_T300_resutls_h5-unknown-train1000-sym1.npz ensemble_models/a3.npz

sgdml all ethanol_T300_resutls_h5.npz 1000 200 1000 --gdml --no_E -o
mv ethanol_T300_resutls_h5-unknown-train1000-sym1.npz ensemble_models/a4.npz

sgdml all ethanol_T300_resutls_h5.npz 1000 200 1000 --gdml --no_E -o
mv ethanol_T300_resutls_h5-unknown-train1000-sym1.npz ensemble_models/a5.npz

sgdml all ethanol_T300_resutls_h5.npz 1000 200 1000 --gdml --no_E -o
mv ethanol_T300_resutls_h5-unknown-train1000-sym1.npz ensemble_models/a6.npz

sgdml all ethanol_T300_resutls_h5.npz 1000 200 1000 --gdml --no_E -o
mv ethanol_T300_resutls_h5-unknown-train1000-sym1.npz ensemble_models/a7.npz

sgdml all ethanol_T300_resutls_h5.npz 1000 200 1000 --gdml --no_E -o
mv ethanol_T300_resutls_h5-unknown-train1000-sym1.npz ensemble_models/a8.npz

sgdml all ethanol_T300_resutls_h5.npz 1000 200 1000 --gdml --no_E -o
mv ethanol_T300_resutls_h5-unknown-train1000-sym1.npz ensemble_models/a9.npz

sgdml all ethanol_T300_resutls_h5.npz 1000 200 1000 --gdml --no_E -o
mv ethanol_T300_resutls_h5-unknown-train1000-sym1.npz ensemble_models/a10.npz