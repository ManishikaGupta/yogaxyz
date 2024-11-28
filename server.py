from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np;
import pandas as pd

app = Flask(__name__)
CORS(app)  # Enable CORS to allow cross-origin requests from React

# Load yoga data from a CSV file

yoga_data = pd.DataFrame({
    "Health Problem": [
        # Skin Problems
        "Skin Problems", "Skin Problems", "Skin Problems", "Skin Problems", "Skin Problems",
        # Anxiety
        "Anxiety", "Anxiety", "Anxiety", "Anxiety", "Anxiety",
        # Asthma
        "Asthma", "Asthma", "Asthma", "Asthma", "Asthma",
        # Back Pain
        "Back Pain", "Back Pain", "Back Pain", "Back Pain", "Back Pain",
        # Digestion
        "Digestion", "Digestion", "Digestion", "Digestion", "Digestion",
        # Eyes Related
        "Eyes Related", "Eyes Related", "Eyes Related", "Eyes Related", "Eyes Related",
        # Blood Pressure (HyperTension)
        "Blood Pressure (HyperTension)", "Blood Pressure (HyperTension)", "Blood Pressure (HyperTension)",
        "Blood Pressure (HyperTension)", "Blood Pressure (HyperTension)",
        # Cardiovascular
        "Cardiovascular", "Cardiovascular", "Cardiovascular", "Cardiovascular", "Cardiovascular",
        # Diabetes
        "Diabetes", "Diabetes", "Diabetes", "Diabetes", "Diabetes",
        # Headache (Migraine)
        "Headache (Migraine)", "Headache (Migraine)", "Headache (Migraine)", "Headache (Migraine)", 
        "Headache (Migraine)",
        # Stress
        "Stress", "Stress", "Stress", "Stress", "Stress",
        # Muscles (Strain, Pull, Soreness)
        "Muscles (Strain, Pull, Soreness)", "Muscles (Strain, Pull, Soreness)", "Muscles (Strain, Pull, Soreness)",
        "Muscles (Strain, Pull, Soreness)", "Muscles (Strain, Pull, Soreness)",
        # Overweight, Obesity
        "Overweight, Obesity", "Overweight, Obesity", "Overweight, Obesity", 
        "Overweight, Obesity", "Overweight, Obesity",
        # Immunity
        "Immunity", "Immunity", "Immunity", "Immunity", "Immunity",
        # Cough, Cold
        "Cough, Cold", "Cough, Cold", "Cough, Cold", "Cough, Cold", "Cough, Cold",
        # Cholesterol
        "Cholesterol", "Cholesterol", "Cholesterol", "Cholesterol", "Cholesterol",
        # Knee Pain
        "Knee Pain", "Knee Pain", "Knee Pain", "Knee Pain", "Knee Pain",
        # Arthritis or Pain
        "Arthritis or Pain", "Arthritis or Pain", "Arthritis or Pain", 
        "Arthritis or Pain", "Arthritis or Pain",
        # Underweight, Muscle Gain"
        "Underweight, Muscle Gain", "Underweight, Muscle Gain", 
        "Underweight, Muscle Gain", "Underweight, Muscle Gain", 
        "Underweight, Muscle Gain",
        # Hair Problems
        "Hair Problems", "Hair Problems", "Hair Problems", 
        "Hair Problems", "Hair Problems"
    ],
    "Yoga Pose Name": [
        # Skin Problems
        "Uttanasana (Standing Forward Bend)", "Trikonasana (Triangle Pose)",
        "Bhujangasana (Cobra Pose)", "Pavanamuktasana (Wind Removing)", 
        "Viparita Karani (Legs Up the Wall)",
        # Anxiety
        "Supta Kapotasana (Pigeon Pose)", "Janu Shirshasana A (Head to Knee Pose)",
        "Sukhasana (Easy Pose)", "Baddha Konasana (Bound Angle Pose)", 
        "Matsyasana (Fish Pose)",
        # Asthma
        "Setu Bandhasana (Bridge Pose)", "Gomukhasana (Cow Pose)", 
        "Dhanurasana (Bow Pose)", "Kapal Bharti", 
        "Alternate Nostril Breathing",
        # Back Pain
        "Ushtrasana (Camel Pose)", "Setu Bandhasana (Bridge Pose)",
        "Ardha Pincha Mayurasana (Dolphin Pose)", 
        "Ardha Chandrasana (Half Moon Pose)", "Parivritta Virasana (Hero Twist)",
        # Digestion
        "Virasana (Hero Pose)", "Padangushthasana (Big Toe Pose)",
        "Ardha Chandrasana (Half Moon Pose)", 
        "Janu Shirshasana A (Head to Knee Pose)", "Virasana (Hero Pose)",
        # Eyes Related
        "Vrikshasana (Tree Pose)", "Palming", "Eye Rotations", "Focus Switching", "Bharmari Pranayam",
        # Blood Pressure (HyperTension)
        "Ardha Pincha Mayurasana (Dolphin Pose)", "Baddha Konasana (Bound Angle Pose)",
        "Paschimottanasana A (Forward Bend - Seated)", "Shavasana (Corpse Pose)", "Balasana (Child's Pose)",
        # Cardiovascular
        "Padangushthasana (Big Toe Pose)", "Uttanasana (Shoulder Stand Pose)", 
        "Paschimottanasana A (Forward Bend - Seated)", "Gomukhasana (Cow Pose)", 
        "Vakrasana (Half Spinal Twist)",
        # Diabetes
        "Dhanurasana (Bow Pose)", "Balasana (Child's Pose)", "Bhekasana (Frog Pose)", 
        "Urdhva Vrikshasana (Tadasana)", "Urdhva Dhanurasana (Wheel Pose)",
        # Headache (Migraine)
        "Viparita Karani (Legs up the Wall)", "Balasana (Child's Pose)", "Shavasana (Corpse Pose)",
        "Setu Bandhasana (Bridge Pose)", "Uttanasana (Standing Forward Bend)",
        # Stress
        "Marjariasana (Cat Pose)", "Viparita Karani (Legs up the Wall)", "Shavasana (Corpse Pose)", 
        "Balasana (Child's Pose)", "Supta Kapotasana (Pigeon Pose)",
        # Muscles (Strain, Pull, Soreness)
        "Shalabhasana (Half Locust Pose)", "Ardha Pincha Mayurasana (Dolphin Pose)", 
        "Chakravakasana (Bird Dog Balance)", "Balasana (Extended Child Pose)", "Supta Kapotasana (Pigeon Pose)",
        # Overweight, Obesity
        "Virabhadrasana (Warrior Pose)", "Trikonasana (Triangle Pose)", 
        "Parivritta Utkatasana (Twisted Chair Pose)", "Dhanurasana (Bow Pose)", 
        "Phalakasana (Plank Pose)",
        # Immunity
        "Shalabhasana (Locust Pose)", "Anjaneyasana (Low Lunge Pose)", 
        "Bakasana (Crow Pose)", "Urdhva Vrikshasana (Tadasana)", 
        "Chaturanga Dandasana (Four-Limbed Staff Pose)",
        # Cough, Cold
        "Sarvangasana (Shoulder Stand)", "Kurmasana (Advanced Tortoise Pose)", 
        "Shirshasana (Head Stand)", "Viparita Karani (Legs up the Wall)", 
        "Trikonasana (Triangle Pose)",
        # Cholesterol
        "Vakrasana (Half Spinal Twist)", "Uttanasana (Forward Bend)", 
        "Chakrasana (Wheel Pose)", "Sarvangasana (Shoulder Stand)", 
        "Paschimottanasana (Seated Forward Bend)",
        # Knee Pain
        "Uttanasana (Standing Forward Bend)", 
        "Upavishta Konasana (Wide-Angled Seated Forward Bend)", 
        "Anjaneyasana (Low Lunge)", "Virabhadrasana (Warrior Pose)", 
        "Chandrasana (High Lunge)",
        # Arthritis or Pain
        "Virabhadrasana (Warrior Pose)", "Vrikshasana (Tree Pose)", 
        "Trikonasana (Triangle Pose)", "Setu Bandhasana (Bridge Pose)", 
        "Salamba Bhujangasana (Sphinx Pose)",
        # Underweight, Muscle Gain
        "Falkasan (Forearm Plank)", "Ardha Pincha Mayurasana (Dolphin Pose)", 
        "Vrikshasana (Tree Pose)", "Malasana (Squat)", "Chandrasana (High Lunge)",
        # Hair Problems
        "Pavanamuktasana (Wind Removing Pose)", "Vajrasana (Thunderbolt Pose)", 
        "Adho Mukha Shvanasana (Downward Dog Pose)", 
        "Uttanasana (Standing Forward Bend)", "Sarvangasana (Shoulder Stand)"
    ],
    "Image URL": [
        # Skin Problems
        "https://pocketyoga.com/assets/images/thumbnails146/ForwardBendBind-tn146.png",
        "https://pocketyoga.com/assets/images/full/TriangleForward_L.png",
        "https://pocketyoga.com/assets/images/full/CorpseDoubleLegRaise.png",
        "https://pocketyoga.com/assets/images/full/Turtle.png",
        "https://pocketyoga.com/assets/images/full/CorpseDoubleLegRaise.png",
        # Anxiety
        "https://pocketyoga.com/assets/images/full/PigeonPose_L.png",
        "https://pocketyoga.com/assets/images/full/HeadToKnee_R.png",
        "https://pocketyoga.com/assets/images/full/EasyPose.png",
        "https://pocketyoga.com/assets/images/full/BoundAnglePose_L.png",
        "https://pocketyoga.com/assets/images/full/FishPose_L.png",
        # Asthma
        "https://pocketyoga.com/assets/images/full/BridgePose.png",
        "https://pocketyoga.com/assets/images/full/CowPose_L.png",
        "https://pocketyoga.com/assets/images/full/BowPose.png",
        "https://pocketyoga.com/assets/images/full/AlternateNostrilBreathing.png",
        "https://pocketyoga.com/assets/images/full/AlternateNostrilBreathing.png",
        # Back Pain
        "https://pocketyoga.com/assets/images/full/CamelPose_L.png",
        "https://pocketyoga.com/assets/images/full/BridgePose.png",
        "https://pocketyoga.com/assets/images/full/DolphinPose_L.png",
        "https://pocketyoga.com/assets/images/full/HalfMoonPose_L.png",
        "https://pocketyoga.com/assets/images/full/HeroPose_L.png",
        # Digestion
        "https://pocketyoga.com/assets/images/full/HeroPose_L.png",
        "https://pocketyoga.com/assets/images/full/BigToePose_L.png",
        "https://pocketyoga.com/assets/images/full/HalfMoonPose_L.png",
        "https://pocketyoga.com/assets/images/full/HeadToKnee_R.png",
        "https://pocketyoga.com/assets/images/full/HeroPose_L.png",
        # Eyes Related
        "https://pocketyoga.com/assets/images/full/TreePose_L.png",
        "https://pocketyoga.com/assets/images/full/Palming.png",
        "https://pocketyoga.com/assets/images/full/EyeRotation.png",
        "https://pocketyoga.com/assets/images/full/FocusSwitching.png",
        "https://pocketyoga.com/assets/images/full/BhramariBreathing.png",
        # Blood Pressure (HyperTension)
        "https://pocketyoga.com/assets/images/full/DolphinPose_L.png",
        "https://pocketyoga.com/assets/images/full/BoundAnglePose_L.png",
        "https://pocketyoga.com/assets/images/full/SeatedForwardBend.png",
        "https://pocketyoga.com/assets/images/full/CorpsePose_L.png",
        "https://pocketyoga.com/assets/images/full/ChildPose_L.png",
        # Cardiovascular
        "https://pocketyoga.com/assets/images/full/BigToePose_L.png",
        "https://pocketyoga.com/assets/images/full/ShoulderStand_L.png",
        "https://pocketyoga.com/assets/images/full/SeatedForwardBend.png",
        "https://pocketyoga.com/assets/images/full/CowPose_L.png",
        "https://pocketyoga.com/assets/images/full/HalfSpinalTwist.png",
        # Diabetes
        "https://pocketyoga.com/assets/images/full/BowPose.png",
        "https://pocketyoga.com/assets/images/full/ChildPose_L.png",
        "https://pocketyoga.com/assets/images/full/FrogPose.png",
        "https://pocketyoga.com/assets/images/full/Tadasana.png",
        "https://pocketyoga.com/assets/images/full/WheelPose.png",
        # Headache (Migraine)
        "https://pocketyoga.com/assets/images/full/LegsUpTheWall.png",
        "https://pocketyoga.com/assets/images/full/ChildPose_L.png",
        "https://pocketyoga.com/assets/images/full/CorpsePose_L.png",
        "https://pocketyoga.com/assets/images/full/BridgePose.png",
        "https://pocketyoga.com/assets/images/full/StandingForwardBend.png",
        # Stress
        "https://pocketyoga.com/assets/images/full/CatPose.png",
        "https://pocketyoga.com/assets/images/full/LegsUpTheWall.png",
        "https://pocketyoga.com/assets/images/full/CorpsePose_L.png",
        "https://pocketyoga.com/assets/images/full/ChildPose_L.png",
        "https://pocketyoga.com/assets/images/full/PigeonPose_L.png",
        # Muscles (Strain, Pull, Soreness)
        "https://pocketyoga.com/assets/images/full/HalfLocustPose.png",
        "https://pocketyoga.com/assets/images/full/DolphinPose_L.png",
        "https://pocketyoga.com/assets/images/full/BirdDogBalance.png",
        "https://pocketyoga.com/assets/images/full/ExtendedChildPose.png",
        "https://pocketyoga.com/assets/images/full/PigeonPose_L.png",
        # Overweight, Obesity
        "https://pocketyoga.com/assets/images/full/WarriorPose_L.png",
        "https://pocketyoga.com/assets/images/full/TrianglePose.png",
        "https://pocketyoga.com/assets/images/full/TwistedChairPose.png",
        "https://pocketyoga.com/assets/images/full/BowPose.png",
        "https://pocketyoga.com/assets/images/full/PlankPose.png",
        # Immunity
        "https://pocketyoga.com/assets/images/full/LocustPose.png",
        "https://pocketyoga.com/assets/images/full/LowLungePose.png",
        "https://pocketyoga.com/assets/images/full/CrowPose.png",
        "https://pocketyoga.com/assets/images/full/Tadasana.png",
        "https://pocketyoga.com/assets/images/full/FourLimbedStaffPose.png",
        # Cough, Cold
        "https://pocketyoga.com/assets/images/full/ShoulderStand.png",
        "https://pocketyoga.com/assets/images/full/AdvancedTortoisePose.png",
        "https://pocketyoga.com/assets/images/full/HeadStand.png",
        "https://pocketyoga.com/assets/images/full/LegsUpTheWall.png",
        "https://pocketyoga.com/assets/images/full/TrianglePose.png",
        # Cholesterol
        "https://pocketyoga.com/assets/images/full/HalfSpinalTwist.png",
        "https://pocketyoga.com/assets/images/full/StandingForwardBend.png",
        "https://pocketyoga.com/assets/images/full/WheelPose.png",
        "https://pocketyoga.com/assets/images/full/ShoulderStand.png",
        "https://pocketyoga.com/assets/images/full/SeatedForwardBend.png",
        # Knee Pain
        "https://pocketyoga.com/assets/images/full/StandingForwardBend.png",
        "https://pocketyoga.com/assets/images/full/WideAngledSeatedForwardBend.png",
        "https://pocketyoga.com/assets/images/full/LowLunge.png",
        "https://pocketyoga.com/assets/images/full/WarriorPose_L.png",
        "https://pocketyoga.com/assets/images/full/HighLunge.png",
        # Arthritis or Pain
        "https://pocketyoga.com/assets/images/full/WarriorPose_L.png",
        "https://pocketyoga.com/assets/images/full/TreePose_L.png",
        "https://pocketyoga.com/assets/images/full/TrianglePose.png",
        "https://pocketyoga.com/assets/images/full/BridgePose.png",
        "https://pocketyoga.com/assets/images/full/SphinxPose.png",
        # Underweight, Muscle Gain
        "https://pocketyoga.com/assets/images/full/ForearmPlank.png",
        "https://pocketyoga.com/assets/images/full/DolphinPose_L.png",
        "https://pocketyoga.com/assets/images/full/TreePose_L.png",
        "https://pocketyoga.com/assets/images/full/SquatPose.png",
        "https://pocketyoga.com/assets/images/full/HighLunge.png",
        # Hair Problems
        "https://pocketyoga.com/assets/images/full/WindRemovingPose.png",
        "https://pocketyoga.com/assets/images/full/ThunderboltPose.png",
        "https://pocketyoga.com/assets/images/full/DownwardDogPose.png",
        "https://pocketyoga.com/assets/images/full/StandingForwardBend.png",
        "https://pocketyoga.com/assets/images/full/ShoulderStand.png"
    ]
})

# Route to fetch all available health problems
@app.route('/health-problems', methods=['GET'])
def get_health_problems():
    health_problems = yoga_data["Health Problem"].unique().tolist()
    return jsonify(health_problems)

# Route to fetch yoga suggestions for selected health problems
@app.route('/suggestions', methods=['POST'])
def get_suggestions():
    data = request.json
    selected_problems = data.get('healthProblems', [])
    
    # Filter yoga poses based on the selected health problems
    filtered_data = yoga_data[yoga_data["Health Problem"].isin(selected_problems)]
    suggestions = filtered_data.to_dict(orient="records")
    return jsonify(suggestions)

if __name__ == "__main__":
    app.run(debug=True)