import pandas as pd
import json

SNOMED_MAP = {
    "270492004": {"acronym": "1AVB",   "name": "1st degree AV block",                    "category": "conduction_block",    "adverse": False},
    "195042002": {"acronym": "2AVB",   "name": "2nd degree AV block",                    "category": "conduction_block",    "adverse": True},
    "54016002":  {"acronym": "2AVB1",  "name": "2nd degree AV block type I",             "category": "conduction_block",    "adverse": True},
    "28189009":  {"acronym": "2AVB2",  "name": "2nd degree AV block type II",            "category": "conduction_block",    "adverse": True},
    "27885002":  {"acronym": "3AVB",   "name": "3rd degree AV block",                    "category": "conduction_block",    "adverse": True},
    "251173003": {"acronym": "ABI",    "name": "Atrial bigeminy",                        "category": "arrhythmia",          "adverse": False},
    "39732003":  {"acronym": "ALS",    "name": "Left axis deviation",                    "category": "axis_deviation",      "adverse": False},
    "284470004": {"acronym": "APB",    "name": "Atrial premature beats",                 "category": "arrhythmia",          "adverse": False},
    "164917005": {"acronym": "AQW",    "name": "Abnormal Q wave",                        "category": "morphology_change",   "adverse": True},
    "47665007":  {"acronym": "ARS",    "name": "Right axis deviation",                   "category": "axis_deviation",      "adverse": False},
    "233917008": {"acronym": "AVB",    "name": "AV block (generic)",                     "category": "conduction_block",    "adverse": True},
    "251199005": {"acronym": "CCR",    "name": "Counterclockwise rotation",              "category": "morphology_change",   "adverse": False},
    "251198002": {"acronym": "CR",     "name": "Clockwise rotation",                     "category": "morphology_change",   "adverse": False},
    "428417006": {"acronym": "ERV",    "name": "Early ventricular repolarization",       "category": "repolarization",      "adverse": False},
    "164942001": {"acronym": "FQRS",   "name": "fQRS wave",                              "category": "morphology_change",   "adverse": False},
    "698252002": {"acronym": "IDC",    "name": "Intraventricular conduction delay",      "category": "conduction_block",    "adverse": False},
    "426995002": {"acronym": "JEB",    "name": "Junctional escape beat",                 "category": "arrhythmia",          "adverse": False},
    "251164006": {"acronym": "JPT",    "name": "Junctional premature beat",              "category": "arrhythmia",          "adverse": False},
    "164909002": {"acronym": "LBBB",   "name": "Left bundle branch block",               "category": "conduction_block",    "adverse": True},
    "164873001": {"acronym": "LVH",    "name": "Left ventricular hypertrophy",           "category": "structural",          "adverse": True},
    "251146004": {"acronym": "LVQRSAL","name": "Low QRS voltage all leads",              "category": "morphology_change",   "adverse": False},
    "251148003": {"acronym": "LVQRSCL","name": "Low QRS voltage chest leads",            "category": "morphology_change",   "adverse": False},
    "251147008": {"acronym": "LVQRSLL","name": "Low QRS voltage limb leads",             "category": "morphology_change",   "adverse": False},
    "164865005": {"acronym": "MI",     "name": "Myocardial infarction",                  "category": "ischemia",            "adverse": True},
    "164947007": {"acronym": "PRIE",   "name": "PR interval prolongation",               "category": "interval_change",     "adverse": False},
    "164912004": {"acronym": "PWC",    "name": "P wave change",                          "category": "morphology_change",   "adverse": False},
    "111975006": {"acronym": "QTIE",   "name": "QT interval prolongation",               "category": "interval_change",     "adverse": True},
    "446358003": {"acronym": "RAH",    "name": "Right atrial hypertrophy",               "category": "structural",          "adverse": False},
    "59118001":  {"acronym": "RBBB",   "name": "Right bundle branch block",              "category": "conduction_block",    "adverse": False},
    "89792004":  {"acronym": "RVH",    "name": "Right ventricular hypertrophy",          "category": "structural",          "adverse": True},
    "429622005": {"acronym": "STDD",   "name": "ST depression",                          "category": "ischemia",            "adverse": True},
    "164930006": {"acronym": "STE",    "name": "ST elevation",                           "category": "ischemia",            "adverse": True},
    "428750005": {"acronym": "STTC",   "name": "ST-T change",                            "category": "repolarization",      "adverse": False},
    "164931005": {"acronym": "STTU",   "name": "ST tilt up",                             "category": "repolarization",      "adverse": False},
    "164934002": {"acronym": "TWC",    "name": "T wave change",                          "category": "repolarization",      "adverse": False},
    "59931005":  {"acronym": "TWO",    "name": "T wave inversion",                       "category": "repolarization",      "adverse": True},
    "164937009": {"acronym": "UW",     "name": "U wave",                                 "category": "morphology_change",   "adverse": False},
    "11157007":  {"acronym": "VB",     "name": "Ventricular bigeminy",                   "category": "arrhythmia",          "adverse": True},
    "75532003":  {"acronym": "VEB",    "name": "Ventricular escape beat",                "category": "arrhythmia",          "adverse": True},
    "13640000":  {"acronym": "VFW",    "name": "Ventricular fusion wave",                "category": "arrhythmia",          "adverse": False},
    "17338001":  {"acronym": "VPB",    "name": "Ventricular premature beat",             "category": "arrhythmia",          "adverse": False},
    "195060002": {"acronym": "VPE",    "name": "Ventricular preexcitation",              "category": "conduction_block",    "adverse": True},
    "251180001": {"acronym": "VET",    "name": "Ventricular escape trigeminy",           "category": "arrhythmia",          "adverse": True},
    "195101003": {"acronym": "WAVN",   "name": "Wandering atrial pacemaker",             "category": "arrhythmia",          "adverse": False},
    "55827005": {"acronym": "LVH2",   "name": "Left ventricular hypertrophy (alt)",      "category": "structural",          "adverse": True},
    "55930002": {"acronym": "RVH2",   "name": "Right ventricular hypertrophy (alt)",     "category": "structural",          "adverse": True},
    "10370003": {"acronym": "PR",     "name": "Pacing rhythm",                           "category": "conduction_block",    "adverse": True},
    "713427006":{"acronym": "CBBB",   "name": "Complete bundle branch block",            "category": "conduction_block",    "adverse": True},
    "427172004": {"acronym": "PAC",   "name": "Premature atrial contraction",            "category": "arrhythmia",          "adverse": False},
    "74390002":  {"acronym": "WPW",    "name": "Wolff-Parkinson-White syndrome",         "category": "conduction_block",    "adverse": True},
    "426177001": {"acronym": "SB",     "name": "Sinus bradycardia",                      "category": "sinus_rhythm",        "adverse": False},
    "426783006": {"acronym": "SR",     "name": "Sinus rhythm (normal)",                  "category": "sinus_rhythm",        "adverse": False},
    "164889003": {"acronym": "AFIB",   "name": "Atrial fibrillation",                    "category": "arrhythmia",          "adverse": True},
    "427084000": {"acronym": "ST",     "name": "Sinus tachycardia",                      "category": "sinus_rhythm",        "adverse": False},
    "164890007": {"acronym": "AF",     "name": "Atrial flutter",                         "category": "arrhythmia",          "adverse": True},
    "427393009": {"acronym": "SA",     "name": "Sinus arrhythmia",                       "category": "sinus_rhythm",        "adverse": False},
    "426761007": {"acronym": "SVT",    "name": "Supraventricular tachycardia",           "category": "arrhythmia",          "adverse": True},
    "713422000": {"acronym": "AT",     "name": "Atrial tachycardia",                     "category": "arrhythmia",          "adverse": True},
    "233896004": {"acronym": "AVNRT",  "name": "AV node reentrant tachycardia",          "category": "arrhythmia",          "adverse": True},
    "233897008": {"acronym": "AVRT",   "name": "AV reentrant tachycardia",               "category": "arrhythmia",          "adverse": True},
}

CATEGORIES = sorted(set(v["category"] for v in SNOMED_MAP.values()))

def map_dx(dx_list):
 
    if isinstance(dx_list, str):
        dx_list = json.loads(dx_list)

    found, unknown = [], []
    for code in dx_list:
        code = str(code).strip()
        if code in SNOMED_MAP:
            found.append(SNOMED_MAP[code])
        else:
            unknown.append(code)

    return {
        "labels":[f["acronym"]  for f in found],
        "categories":list(set(f["category"] for f in found)),
        "is_adverse": any(f["adverse"] for f in found),
        "snomed_found": [c for c in dx_list if str(c).strip() in SNOMED_MAP],
        "snomed_unknown": unknown,
    }


def enrich_parquet(parquet_path, output_path):
    df = pd.read_parquet(parquet_path)
    print(f"Registros cargados: {len(df)}")

    mapped = df["dx"].apply(map_dx)
    df["labels"] = mapped.apply(lambda x: x["labels"])
    df["categories"] = mapped.apply(lambda x: x["categories"])
    df["is_adverse"] = mapped.apply(lambda x: x["is_adverse"])
    df["snomed_unknown"] = mapped.apply(lambda x: x["snomed_unknown"])

    for cat in CATEGORIES:
        df[f"cat_{cat}"] = df["categories"].apply(lambda x: int(cat in x))

    unknown_all = df["snomed_unknown"].explode().dropna()
    unknown_all = unknown_all[unknown_all != ""]
    print(f"\nCódigos no reconocidos (top-10): {unknown_all.value_counts().head(10).to_dict()}")
    print(f"Registros adversos: {df['is_adverse'].sum()} ({df['is_adverse'].mean()*100:.1f}%)")
    print(f"Distribución de categorías:")
    for cat in CATEGORIES:
        n = df[f"cat_{cat}"].sum()
        print(f"  {cat:30s}: {n:6d} ({n/len(df)*100:.1f}%)")

    df.to_parquet(output_path, index=False)
    print(f"\nParquet enriquecido guardado → {output_path}")
    return df


if __name__ == "__main__":
    df_enriched = enrich_parquet(
        parquet_path="./ml_dataset.parquet",
        output_path="./ml_dataset_enriched.parquet"
    )