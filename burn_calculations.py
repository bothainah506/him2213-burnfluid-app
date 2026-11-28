"""Input, validation, and educational estimates for the fictional BurnFluid app.

This module provides an illustrative classroom formula estimate only. It
does not provide clinical advice, a treatment order, or a verified hospital
protocol.
"""

import math
import re


EDUCATIONAL_DISCLAIMER = (
    "EDUCATIONAL USE ONLY: This fictional patient tool is for learning and "
    "demonstration only. Formula outputs are not a verified hospital "
    "protocol or treatment order, and are not a substitute for professional "
    "medical assessment or clinical advice."
)

EMIRATES_ID_PATTERN = re.compile(r"^784-0000-[0-9]{7}-[0-9]$")

# Traditional illustrative Parkland factor for classroom simulation only.
# This is not a verified hospital protocol or a treatment order.
PROTOCOL_FACTOR = 4.0

# Classroom-only safeguard: do not show an hourly estimate when six minutes
# or less (0.1 hour) remain in the phase. This arbitrary numerical buffer
# prevents a very small divisor from producing an unusually large result.
# It is not a clinical threshold or a recommended treatment boundary.
MIN_REMAINING_HOURS_FOR_CLASSROOM_ESTIMATE = 0.1


def is_at_or_below_classroom_time_threshold(remaining_hours):
    """Check the classroom time safeguard, including floating-point equality.

    The absolute tolerance accounts for tiny representation differences when
    subtracting times such as 24 - 23.9. Relative tolerance is zero so the
    comparison uses only this small, fixed tolerance around the threshold.
    """
    return (
        remaining_hours <= MIN_REMAINING_HOURS_FOR_CLASSROOM_ESTIMATE
        or math.isclose(
            remaining_hours,
            MIN_REMAINING_HOURS_FOR_CLASSROOM_ESTIMATE,
            rel_tol=0.0,
            abs_tol=1e-12,
        )
    )


def print_educational_disclaimer():
    """Print a clear disclaimer before any patient information is collected."""
    print(EDUCATIONAL_DISCLAIMER)


def validate_emirates_id(emirates_id):
    """Return a stripped ID if it is in the fixed fictional 784-0000 format."""
    if not isinstance(emirates_id, str):
        raise ValueError("Emirates ID must be text.")

    emirates_id = emirates_id.strip()
    if not EMIRATES_ID_PATTERN.fullmatch(emirates_id):
        raise ValueError(
            "Emirates ID must use the format 784-0000-0000001-0."
        )
    return emirates_id


def validate_patient_name(patient_name):
    """Return a stripped patient name if it is not empty."""
    if not isinstance(patient_name, str):
        raise ValueError("Patient name must be text.")

    patient_name = patient_name.strip()
    if patient_name == "":
        raise ValueError("Patient name cannot be empty.")
    return patient_name


def validate_patient_age(patient_age):
    """Return an integer age when it is from 18 through 120."""
    if isinstance(patient_age, bool):
        raise ValueError("Age must be a whole number.")

    try:
        age_text = str(patient_age).strip()
        if not re.fullmatch(r"[+-]?\d+", age_text):
            raise ValueError("Age must be a whole number.")
        age = int(age_text)
    except (TypeError, ValueError, OverflowError):
        raise ValueError("Age must be a whole number.")

    if age < 18 or age > 120:
        raise ValueError("Age must be between 18 and 120.")
    return age


def validate_finite_number(value, field_name):
    """Convert a value to float and reject NaN or infinity values."""
    if isinstance(value, bool):
        raise ValueError(field_name + " must be a number.")

    try:
        number = float(value)
    except (TypeError, ValueError, OverflowError):
        raise ValueError(field_name + " must be a number.")

    if not math.isfinite(number):
        raise ValueError(field_name + " must be a finite number.")
    return number


def validate_patient_weight(patient_weight_kg):
    """Return weight in kg if it is from 30 through 250."""
    weight = validate_finite_number(patient_weight_kg, "Weight")
    if weight < 30 or weight > 250:
        raise ValueError("Weight must be between 30 and 250 kg.")
    return weight


def validate_tbsa(tbsa_percent):
    """Return TBSA as a percentage if it is from 20 through 100."""
    tbsa = validate_finite_number(tbsa_percent, "TBSA")
    if tbsa < 20 or tbsa > 100:
        raise ValueError("TBSA must be between 20 and 100 percent.")
    return tbsa


def validate_hours_since_burn(hours_since_burn):
    """Return hours since the burn, not since hospital arrival.

    Valid injury time is from 0 hours (inclusive) up to, but not including,
    24 hours.
    """
    hours = validate_finite_number(
        hours_since_burn, "Hours since the burn injury"
    )
    if hours < 0 or hours >= 24:
        raise ValueError(
            "Hours since burn injury must be 0 or more and less than 24."
        )
    return hours


def validate_fluid_given(fluid_given_ml):
    """Return fluid received during the selected phase in ml, if non-negative.

    This is the amount received during the selected fluid phase.  It is not
    necessarily the cumulative volume received since the burn injury.
    """
    fluid_volume = validate_finite_number(
        fluid_given_ml, "Fluid received during the selected phase"
    )
    if fluid_volume < 0:
        raise ValueError(
            "Fluid received during the selected phase cannot be negative."
        )
    return fluid_volume


def validate_fluid_phase(fluid_phase):
    """Normalize and validate the selected resuscitation phase."""
    if not isinstance(fluid_phase, str):
        raise ValueError("Fluid phase must be text.")

    fluid_phase = fluid_phase.strip().lower()
    valid_phases = ("first_8h", "next_16h", "unknown")
    if fluid_phase not in valid_phases:
        raise ValueError(
            "Fluid phase must be first_8h, next_16h, or unknown."
        )
    return fluid_phase


def validate_inhalation_injury(inhalation_injury):
    """Convert Y/N text (or Boolean text) to a Boolean."""
    if isinstance(inhalation_injury, bool):
        return inhalation_injury

    if not isinstance(inhalation_injury, str):
        raise ValueError("Inhalation injury must be Y or N.")

    answer = inhalation_injury.strip().lower()
    if answer == "y":
        return True
    if answer == "n":
        return False
    raise ValueError("Inhalation injury must be Y or N.")


def prompt_text(prompt):
    """Prompt for text and return None if Ctrl+C or EOF cancels input."""
    try:
        return input(prompt)
    except (EOFError, KeyboardInterrupt):
        print("\nPatient data collection cancelled.")
        return None


def get_valid_emirates_id():
    """Repeat the Emirates ID prompt until it passes validation."""
    while True:
        answer = prompt_text(
            "Fictional Emirates ID (784-0000-0000001-0): "
        )
        if answer is None:
            return None
        try:
            return validate_emirates_id(answer)
        except ValueError as error:
            print("Invalid input:", error)


def get_valid_patient_name():
    """Repeat the patient name prompt until it is non-empty."""
    while True:
        answer = prompt_text("Fictional patient name: ")
        if answer is None:
            return None
        try:
            return validate_patient_name(answer)
        except ValueError as error:
            print("Invalid input:", error)


def get_valid_patient_age():
    """Repeat the age prompt until a whole number from 18 to 120 is entered."""
    while True:
        answer = prompt_text("Patient age (18-120): ")
        if answer is None:
            return None
        try:
            return validate_patient_age(answer)
        except ValueError as error:
            print("Invalid input:", error)


def get_valid_patient_weight():
    """Repeat the weight prompt until 30 through 250 kg is entered."""
    while True:
        answer = prompt_text("Patient weight in kg (30-250): ")
        if answer is None:
            return None
        try:
            return validate_patient_weight(answer)
        except ValueError as error:
            print("Invalid input:", error)


def get_valid_tbsa():
    """Repeat the TBSA prompt until 20 through 100 percent is entered."""
    while True:
        answer = prompt_text("TBSA burn percentage (20-100): ")
        if answer is None:
            return None
        try:
            return validate_tbsa(answer)
        except ValueError as error:
            print("Invalid input:", error)


def get_valid_hours_since_burn():
    """Repeat the injury-time prompt until a value from 0 to under 24."""
    while True:
        answer = prompt_text(
            "Hours since burn injury (0 to less than 24): "
        )
        if answer is None:
            return None
        try:
            return validate_hours_since_burn(answer)
        except ValueError as error:
            print("Invalid input:", error)


def get_valid_fluid_given():
    """Repeat until the phase fluid volume is finite and non-negative."""
    while True:
        answer = prompt_text(
            "Fluid received during the selected phase in ml "
            "(0 or greater): "
        )
        if answer is None:
            return None
        try:
            return validate_fluid_given(answer)
        except ValueError as error:
            print("Invalid input:", error)


def get_valid_fluid_phase():
    """Repeat the phase prompt until a supported value is entered."""
    while True:
        answer = prompt_text(
            "Fluid phase (first_8h, next_16h, or unknown): "
        )
        if answer is None:
            return None
        try:
            return validate_fluid_phase(answer)
        except ValueError as error:
            print("Invalid input:", error)


def get_valid_inhalation_injury():
    """Repeat the inhalation prompt until Y or N is entered."""
    while True:
        answer = prompt_text("Inhalation injury (Y/N): ")
        if answer is None:
            return None
        try:
            return validate_inhalation_injury(answer)
        except ValueError as error:
            print("Invalid input:", error)


def collect_patient_data():
    """Prompt for, validate, and return one fictional patient dictionary."""
    print_educational_disclaimer()

    emirates_id = get_valid_emirates_id()
    if emirates_id is None:
        return None

    patient_name = get_valid_patient_name()
    if patient_name is None:
        return None

    patient_age = get_valid_patient_age()
    if patient_age is None:
        return None

    patient_weight_kg = get_valid_patient_weight()
    if patient_weight_kg is None:
        return None

    tbsa_percent = get_valid_tbsa()
    if tbsa_percent is None:
        return None

    hours_since_burn = get_valid_hours_since_burn()
    if hours_since_burn is None:
        return None

    fluid_given_ml = get_valid_fluid_given()
    if fluid_given_ml is None:
        return None

    fluid_phase = get_valid_fluid_phase()
    if fluid_phase is None:
        return None

    inhalation_injury = get_valid_inhalation_injury()
    if inhalation_injury is None:
        return None

    return {
        "emirates_id": emirates_id,
        "patient_name": patient_name,
        "patient_age": patient_age,
        "patient_weight_kg": patient_weight_kg,
        "tbsa_percent": tbsa_percent,
        "hours_since_burn": hours_since_burn,
        "fluid_given_ml": fluid_given_ml,
        "fluid_phase": fluid_phase,
        "inhalation_injury": inhalation_injury,
    }


def estimate_burn_fluids(patient_data):
    """Return a structured, educational estimate for a validated patient.

    The illustrative formula is factor x weight in kg x TBSA percent. Half
    of that 24-hour volume is assigned to the first 8 hours after injury and
    half to the next 16 hours. The recorded fluid volume is interpreted only
    as fluid received during the phase named in ``fluid_phase``.

    Results never constitute a treatment order or prescribed infusion rate.
    Invalid data returns an error status; uncertain or mismatched phase data
    returns a review status. In both cases, no hourly estimate is provided.
    """
    results = {
        "status": "error",
        "message": "",
        "protocol_factor": PROTOCOL_FACTOR,
        "illustrative_24h_volume_ml": None,
        "first_8h_target_ml": None,
        "next_16h_target_ml": None,
        "current_phase": None,
        "recorded_fluid_phase": None,
        "current_phase_target_ml": None,
        "fluid_given_ml": None,
        "remaining_current_phase_ml": None,
        "remaining_hours_in_current_phase": None,
        "illustrative_average_hourly_rate_ml_per_hour": None,
        "inhalation_injury": None,
    }

    required_keys = (
        "emirates_id",
        "patient_name",
        "patient_age",
        "patient_weight_kg",
        "tbsa_percent",
        "hours_since_burn",
        "fluid_given_ml",
        "fluid_phase",
        "inhalation_injury",
    )
    if not isinstance(patient_data, dict):
        results["message"] = "Patient data is missing or must be a dictionary."
        return results

    for key in required_keys:
        if key not in patient_data:
            results["message"] = "Patient data is missing: " + key + "."
            return results

    # Revalidate the dictionary instead of assuming callers used the prompts.
    try:
        validate_emirates_id(patient_data["emirates_id"])
        validate_patient_name(patient_data["patient_name"])
        validate_patient_age(patient_data["patient_age"])
        weight_kg = validate_patient_weight(patient_data["patient_weight_kg"])
        tbsa_percent = validate_tbsa(patient_data["tbsa_percent"])
        hours_since_burn = validate_hours_since_burn(
            patient_data["hours_since_burn"]
        )
        fluid_given_ml = validate_fluid_given(patient_data["fluid_given_ml"])
        fluid_phase = validate_fluid_phase(patient_data["fluid_phase"])
        inhalation_injury = validate_inhalation_injury(
            patient_data["inhalation_injury"]
        )
    except (TypeError, ValueError, OverflowError) as error:
        results["message"] = "Patient data is invalid: " + str(error)
        return results

    results["inhalation_injury"] = inhalation_injury
    results["fluid_given_ml"] = fluid_given_ml
    results["recorded_fluid_phase"] = fluid_phase

    # These are illustrative estimates, not clinical targets or orders.
    total_volume_ml = PROTOCOL_FACTOR * weight_kg * tbsa_percent
    phase_target_ml = total_volume_ml / 2
    if not math.isfinite(total_volume_ml) or not math.isfinite(phase_target_ml):
        results["message"] = (
            "A calculated volume is not finite; no estimate is available."
        )
        return results

    results["illustrative_24h_volume_ml"] = total_volume_ml
    results["first_8h_target_ml"] = phase_target_ml
    results["next_16h_target_ml"] = phase_target_ml

    # The phase is determined by elapsed time since the burn injury.
    if hours_since_burn < 8:
        current_phase = "first_8h"
        remaining_hours = 8 - hours_since_burn
    elif hours_since_burn < 24:
        current_phase = "next_16h"
        remaining_hours = 24 - hours_since_burn
    else:
        results["status"] = "error"
        results["message"] = (
            "Hours since burn injury are outside the educational prototype "
            "range."
        )
        return results

    results["current_phase"] = current_phase
    results["current_phase_target_ml"] = phase_target_ml
    results["remaining_hours_in_current_phase"] = remaining_hours

    if fluid_phase == "unknown":
        results["status"] = "review"
        results["message"] = (
            "Fluid administration phase is unknown; review the timing before "
            "estimating a rate."
        )
        return results

    if fluid_phase != current_phase:
        results["status"] = "review"
        results["message"] = (
            "Recorded fluid phase does not match the current phase based on "
            "hours since burn injury."
        )
        return results

    if fluid_given_ml > phase_target_ml:
        results["status"] = "review"
        results["message"] = (
            "Recorded fluid volume exceeds the illustrative current-phase "
            "target; review the entry."
        )
        return results

    remaining_volume_ml = phase_target_ml - fluid_given_ml
    results["remaining_current_phase_ml"] = remaining_volume_ml
    if remaining_volume_ml < 0 or remaining_hours <= 0:
        results["status"] = "review"
        results["message"] = (
            "A non-negative phase remainder and positive remaining time are "
            "required for an educational estimate."
        )
        return results

    if is_at_or_below_classroom_time_threshold(remaining_hours):
        results["status"] = "review"
        results["message"] = (
            "Too little time remains for a meaningful classroom estimate. "
            "The hourly estimate is withheld by an arbitrary educational "
            "safeguard, not a clinical threshold."
        )
        return results

    hourly_rate_ml_per_hour = remaining_volume_ml / remaining_hours
    calculated_values = (
        remaining_volume_ml,
        remaining_hours,
        hourly_rate_ml_per_hour,
    )
    for value in calculated_values:
        if not math.isfinite(value):
            results["status"] = "error"
            results["message"] = (
                "A calculated value is not finite; no rate is available."
            )
            return results

    if hourly_rate_ml_per_hour < 0:
        results["status"] = "error"
        results["message"] = (
            "A negative rate is not valid; no rate is available."
        )
        return results

    results["illustrative_average_hourly_rate_ml_per_hour"] = (
        hourly_rate_ml_per_hour
    )
    results["status"] = "educational_estimate"
    results["message"] = (
        "Educational estimate only; not a prescribed infusion rate or "
        "treatment order."
    )
    return results


def generate_safety_alerts(patient_data, calculation_results):
    """Return educational warnings based on patient and estimate data.

    The inhalation warning is checked independently, so it remains visible
    even when another patient field is invalid or the estimate needs review.
    Alerts are educational reminders, not clinical decisions or instructions.
    """
    alerts = []
    required_keys = (
        "emirates_id",
        "patient_name",
        "patient_age",
        "patient_weight_kg",
        "tbsa_percent",
        "hours_since_burn",
        "fluid_given_ml",
        "fluid_phase",
        "inhalation_injury",
    )

    if not isinstance(patient_data, dict):
        alerts.append(
            "Patient data is missing or incomplete; no educational estimate "
            "should be relied on."
        )
        return alerts

    # Check inhalation injury alone before validating the remaining fields.
    try:
        inhalation_injury = validate_inhalation_injury(
            patient_data.get("inhalation_injury")
        )
        if inhalation_injury:
            alerts.append(
                "Inhalation injury is reported. This educational tool does "
                "not assess its effects or provide clinical guidance."
            )
    except (TypeError, ValueError, OverflowError):
        pass

    # Validate fields one at a time so one bad value does not hide other
    # applicable warnings such as unknown timing or the inhalation report.
    field_validators = {
        "emirates_id": validate_emirates_id,
        "patient_name": validate_patient_name,
        "patient_age": validate_patient_age,
        "patient_weight_kg": validate_patient_weight,
        "tbsa_percent": validate_tbsa,
        "hours_since_burn": validate_hours_since_burn,
        "fluid_given_ml": validate_fluid_given,
        "fluid_phase": validate_fluid_phase,
        "inhalation_injury": validate_inhalation_injury,
    }
    valid_patient_values = {}
    patient_data_is_valid = True
    for key in required_keys:
        if key not in patient_data:
            patient_data_is_valid = False
        else:
            try:
                valid_patient_values[key] = field_validators[key](
                    patient_data[key]
                )
            except (TypeError, ValueError, OverflowError):
                patient_data_is_valid = False

    if not patient_data_is_valid:
        alerts.append(
            "Patient data is invalid or incomplete for this educational "
            "prototype; check all required fictional patient fields."
        )

    fluid_phase = valid_patient_values.get("fluid_phase")
    if fluid_phase == "unknown":
        alerts.append(
            "Fluid administration phase is unknown; verify the phase timing "
            "before interpreting any estimate."
        )

    if not isinstance(calculation_results, dict):
        alerts.append(
            "Calculation results are unavailable or invalid; review the "
            "patient data and estimate."
        )
        return alerts

    current_phase = calculation_results.get("current_phase")
    if current_phase is None:
        hours_since_burn = valid_patient_values.get("hours_since_burn")
        if hours_since_burn is not None:
            if hours_since_burn < 8:
                current_phase = "first_8h"
            else:
                current_phase = "next_16h"

    if (
        fluid_phase is not None
        and fluid_phase != "unknown"
        and fluid_phase != current_phase
        and current_phase in ("first_8h", "next_16h")
    ):
        alerts.append(
            "Recorded fluid phase does not match the current phase based on "
            "hours since burn injury."
        )

    target_ml = calculation_results.get("current_phase_target_ml")
    if target_ml is None:
        target_ml = calculation_results.get("first_8h_target_ml")
        if current_phase == "next_16h":
            target_ml = calculation_results.get("next_16h_target_ml")
    if target_ml is None:
        weight_kg = valid_patient_values.get("patient_weight_kg")
        tbsa_percent = valid_patient_values.get("tbsa_percent")
        if weight_kg is not None and tbsa_percent is not None:
            # Reconstruct only the classroom target if other invalid fields
            # caused the estimator to stop before populating its result.
            target_ml = PROTOCOL_FACTOR * weight_kg * tbsa_percent / 2

    try:
        target_ml = validate_finite_number(
            target_ml, "Illustrative phase target"
        )
        recorded_fluid_ml = valid_patient_values.get("fluid_given_ml")
        if recorded_fluid_ml is not None and recorded_fluid_ml > target_ml:
            alerts.append(
                "Recorded fluid volume exceeds the illustrative phase "
                "target; review the recorded value."
            )
    except (TypeError, ValueError, OverflowError):
        # Invalid patient information has already received its own warning.
        pass

    remaining_hours = calculation_results.get(
        "remaining_hours_in_current_phase"
    )
    if remaining_hours is None:
        hours_since_burn = valid_patient_values.get("hours_since_burn")
        if hours_since_burn is not None:
            if hours_since_burn < 8:
                remaining_hours = 8 - hours_since_burn
            else:
                remaining_hours = 24 - hours_since_burn

    if remaining_hours is not None:
        try:
            remaining_hours = validate_finite_number(
                remaining_hours, "Remaining phase time"
            )
            if is_at_or_below_classroom_time_threshold(remaining_hours):
                alerts.append(
                    "Insufficient remaining time for a meaningful classroom "
                    "hourly estimate; the estimate is withheld by an "
                    "educational numerical safeguard."
                )
        except (TypeError, ValueError, OverflowError):
            alerts.append(
                "Remaining phase time is unavailable; review the estimate "
                "inputs."
            )
    elif patient_data_is_valid:
        alerts.append(
            "Remaining phase time is unavailable; review the estimate inputs."
        )

    return alerts


if __name__ == "__main__":
    patient = collect_patient_data()
    if patient is not None:
        print("\nValidated patient data:")
        for key, value in patient.items():
            print(key + ":", value)