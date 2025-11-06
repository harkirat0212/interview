

# """
# Main Integration File - AI Interview System
# Professional UI with cleaner design
# """

# import streamlit as st
# import warnings
# import os
# from PIL import Image, ImageDraw

# # Import the three modular systems
# from Recording_system import RecordingSystem
# from analysis_system import AnalysisSystem
# from scoring_dashboard import ScoringDashboard

# warnings.filterwarnings('ignore')
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# # Try importing optional modules
# try:
#     import mediapipe as mp
#     MP_AVAILABLE = True
#     mp_face_mesh = mp.solutions.face_mesh
#     mp_hands = mp.solutions.hands
# except:
#     MP_AVAILABLE = False

# try:
#     from ultralytics import YOLO
#     YOLO_AVAILABLE = True
# except:
#     YOLO_AVAILABLE = False

# try:
#     from sentence_transformers import SentenceTransformer
#     SENTENCE_TRANSFORMER_AVAILABLE = True
# except:
#     SENTENCE_TRANSFORMER_AVAILABLE = False

# try:
#     from deepface import DeepFace
#     DEEPFACE_AVAILABLE = True
# except:
#     DEEPFACE_AVAILABLE = False

# # ==================== PAGE CONFIG ====================
# st.set_page_config(page_title="Interview Assessment Platform", layout="wide", page_icon="🎯")

# # ==================== PROFESSIONAL STYLES ====================
# st.markdown("""
# <style>
# /* Global Styles */
# body { 
#     background-color: #f5f7fa; 
#     color: #2c3e50; 
#     font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
# }

# /* Hide Streamlit branding */
# #MainMenu {visibility: hidden;}
# footer {visibility: hidden;}
# header {visibility: hidden;}

# /* Main Title */
# .main-title { 
#     font-size: 2.2rem; 
#     font-weight: 600; 
#     text-align: center; 
#     color: #1e3a8a; 
#     margin-bottom: 0.5rem;
#     letter-spacing: -0.5px;
# }

# .subtext { 
#     text-align: center; 
#     color: #64748b; 
#     margin-bottom: 2rem; 
#     font-size: 1rem;
#     font-weight: 400;
# }

# /* Question Display */
# .question-box { 
#     background: white; 
#     padding: 30px; 
#     border-radius: 12px; 
#     border-left: 4px solid #3b82f6; 
#     font-size: 1.1rem; 
#     margin-bottom: 1.5rem; 
#     min-height: 400px;
#     box-shadow: 0 1px 3px rgba(0,0,0,0.08);
# }

# .question-box h2 {
#     color: #1e40af;
#     font-size: 1.3rem;
#     font-weight: 600;
#     margin-bottom: 20px;
#     padding-bottom: 12px;
#     border-bottom: 1px solid #e2e8f0;
# }

# .question-box .question-text {
#     color: #334155;
#     font-size: 1.05rem;
#     line-height: 1.7;
#     margin-top: 20px;
#     font-weight: 400;
# }

# .question-box .question-meta {
#     color: #64748b;
#     font-size: 0.9rem;
#     margin-top: 20px;
#     padding-top: 15px;
#     border-top: 1px solid #f1f5f9;
# }

# /* Cards and Metrics */
# .metric-card { 
#     background: white; 
#     border-radius: 10px; 
#     padding: 20px; 
#     text-align: center; 
#     box-shadow: 0 1px 3px rgba(0,0,0,0.08); 
#     margin-bottom: 1rem;
#     border: 1px solid #e2e8f0;
# }

# .metric-card h3 { 
#     color: #1e40af; 
#     font-size: 1.6rem; 
#     margin-bottom: 5px;
#     font-weight: 600;
# }

# .metric-card p { 
#     color: #64748b; 
#     font-size: 0.85rem; 
#     margin: 0;
#     font-weight: 500;
# }

# /* Status Boxes */
# .success-box { 
#     background: #f0fdf4; 
#     padding: 16px; 
#     border-radius: 8px; 
#     border-left: 4px solid #22c55e; 
#     margin: 15px 0;
#     color: #166534;
# }

# .warning-box { 
#     background: #fffbeb; 
#     padding: 16px; 
#     border-radius: 8px; 
#     border-left: 4px solid #f59e0b; 
#     margin: 15px 0;
#     color: #92400e;
# }

# .error-box { 
#     background: #fef2f2; 
#     padding: 16px; 
#     border-radius: 8px; 
#     border-left: 4px solid #ef4444; 
#     margin: 15px 0;
#     color: #991b1b;
# }

# /* Guideline Box */
# .guideline-box { 
#     background: white; 
#     padding: 25px; 
#     border-radius: 12px; 
#     border: 1px solid #e2e8f0; 
#     margin: 25px 0;
#     box-shadow: 0 1px 3px rgba(0,0,0,0.08);
# }

# .guideline-box h2 {
#     color: #1e40af;
#     font-size: 1.4rem;
#     font-weight: 600;
#     margin-bottom: 15px;
# }

# /* Demo Boxes */
# .correct-demo { 
#     background: #f0fdf4; 
#     border: 2px solid #22c55e; 
#     border-radius: 10px; 
#     padding: 20px;
# }

# .incorrect-demo { 
#     background: #fef2f2; 
#     border: 2px solid #ef4444; 
#     border-radius: 10px; 
#     padding: 20px;
# }

# /* Video Container */
# .video-container {
#     position: sticky;
#     top: 20px;
#     background: #000;
#     border-radius: 10px;
#     padding: 10px;
#     box-shadow: 0 4px 6px rgba(0,0,0,0.1);
# }

# /* Buttons */
# .stButton > button {
#     border-radius: 8px;
#     font-weight: 500;
#     transition: all 0.2s;
# }

# .stButton > button:hover {
#     transform: translateY(-1px);
#     box-shadow: 0 4px 6px rgba(0,0,0,0.1);
# }

# /* Progress Bar */
# .stProgress > div > div {
#     background-color: #3b82f6;
# }

# /* Expander */
# .streamlit-expanderHeader {
#     background-color: white;
#     border-radius: 8px;
#     border: 1px solid #e2e8f0;
# }

# /* Hide sidebar */
# [data-testid="stSidebar"] {
#     display: none;
# }
# </style>
# """, unsafe_allow_html=True)

# # ==================== QUESTIONS CONFIGURATION ====================
# QUESTIONS = [
#     {
#         "question": "Tell me about yourself.",
#         "type": "personal",
#         "ideal_answer": "I'm a computer science postgraduate with a strong interest in AI and software development. I've worked on several projects involving Python, machine learning, and data analysis, which helped me improve both my technical and problem-solving skills. I enjoy learning new technologies and applying them to create practical solutions. Outside of academics, I like collaborating on team projects and continuously developing my professional skills.",
#         "tip": "Focus on your background, skills, and personality"
#     },
#     {
#         "question": "What are your strengths and weaknesses?",
#         "type": "personal",
#         "ideal_answer": "One of my key strengths is that I'm very detail-oriented and persistent – I make sure my work is accurate and well-tested. I also enjoy solving complex problems and learning new tools quickly. As for weaknesses, I used to spend too much time perfecting small details, which sometimes slowed me down. But I've been improving by prioritizing tasks better and focusing on overall impact.",
#         "tip": "Be honest and show self-awareness"
#     },
#     {
#         "question": "Where do you see yourself in the next 5 years?",
#         "type": "personal",
#         "ideal_answer": "In the next five years, I see myself growing into a more responsible and skilled professional, ideally in a role where I can contribute to meaningful projects involving AI and software development. I'd also like to take on leadership responsibilities and guide new team members as I gain experience.",
#         "tip": "Show ambition aligned with career growth"
#     }
# ]

# # ==================== GENERATE DEMO IMAGES ====================
# def create_frame_demo_image(is_correct=True):
#     """Create demonstration image showing correct/incorrect positioning"""
#     width, height = 600, 400
#     img = Image.new('RGB', (width, height), color='#f5f7fa')
#     draw = ImageDraw.Draw(img)
    
#     margin = 50
#     boundary_color = '#22c55e' if is_correct else '#ef4444'
    
#     # Draw boundaries
#     draw.line([(margin, 0), (margin, height)], fill=boundary_color, width=4)
#     draw.line([(width-margin, 0), (width-margin, height)], fill=boundary_color, width=4)
#     draw.line([(0, margin), (width, margin)], fill=boundary_color, width=4)
#     draw.rectangle([margin, margin, width-margin, height], outline=boundary_color, width=3)
    
#     if is_correct:
#         # Draw person inside boundaries
#         head_center_x = width // 2
#         head_center_y = margin + 80
#         head_radius = 40
#         draw.ellipse([head_center_x - head_radius, head_center_y - head_radius,
#                      head_center_x + head_radius, head_center_y + head_radius],
#                     fill='#fbbf24', outline='#22c55e', width=2)
        
#         body_top = head_center_y + head_radius + 10
#         body_width = 80
#         body_height = 120
#         draw.rectangle([head_center_x - body_width//2, body_top,
#                        head_center_x + body_width//2, body_top + body_height],
#                       fill='#3b82f6', outline='#22c55e', width=2)
        
#         draw.rectangle([head_center_x - body_width//2 - 20, body_top + 20,
#                        head_center_x - body_width//2, body_top + 80],
#                       fill='#fbbf24', outline='#22c55e', width=2)
#         draw.rectangle([head_center_x + body_width//2, body_top + 20,
#                        head_center_x + body_width//2 + 20, body_top + 80],
#                       fill='#fbbf24', outline='#22c55e', width=2)
        
#         check_size = 30
#         check_x = width - 80
#         check_y = 80
#         draw.line([(check_x, check_y + check_size//2), (check_x + check_size//3, check_y + check_size)],
#                  fill='#22c55e', width=5)
#         draw.line([(check_x + check_size//3, check_y + check_size), (check_x + check_size, check_y)],
#                  fill='#22c55e', width=5)
        
#         draw.text((width//2, height - 30), "✅ CORRECT: Stay within boundaries", 
#                  fill='#22c55e', anchor="mm", font=None)
#     else:
#         # Draw person outside boundaries
#         head_center_x = margin - 30
#         head_center_y = margin + 80
#         head_radius = 40
#         draw.ellipse([head_center_x - head_radius, head_center_y - head_radius,
#                      head_center_x + head_radius, head_center_y + head_radius],
#                     fill='#fbbf24', outline='#ef4444', width=2)
        
#         body_top = head_center_y + head_radius + 10
#         body_width = 80
#         body_height = 120
#         draw.rectangle([head_center_x - body_width//2, body_top,
#                        head_center_x + body_width//2, body_top + body_height],
#                       fill='#3b82f6', outline='#ef4444', width=2)
        
#         other_x = width - margin + 20
#         other_y = margin + 80
#         draw.ellipse([other_x - 30, other_y - 30, other_x + 30, other_y + 30],
#                     fill='#fbbf24', outline='#ef4444', width=2)
        
#         x_size = 30
#         x_x = width - 80
#         x_y = 80
#         draw.line([(x_x, x_y), (x_x + x_size, x_y + x_size)], fill='#ef4444', width=5)
#         draw.line([(x_x + x_size, x_y), (x_x, x_y + x_size)], fill='#ef4444', width=5)
        
#         draw.text((width//2, height - 30), "❌ INCORRECT: Outside boundaries", 
#                  fill='#ef4444', anchor="mm", font=None)
    
#     return img

# # ==================== HOME PAGE ====================
# def show_home_page():
#     """Display professional home page"""
    
#     # Hero Section
#     st.markdown("""
#     <div style="text-align: center; padding: 40px 0 30px 0;">
#         <h1 style="font-size: 2.5rem; font-weight: 700; color: #1e3a8a; margin-bottom: 10px; letter-spacing: -0.5px;">
#             Interview Assessment Platform
#         </h1>
#         <p style="font-size: 1.1rem; color: #64748b; font-weight: 400; max-width: 700px; margin: 0 auto;">
#             Professional evaluation system for structured video interviews with comprehensive analytics
#         </p>
#     </div>
#     """, unsafe_allow_html=True)
    
#     # Key Features
#     col_feat1, col_feat2, col_feat3 = st.columns(3)
    
#     with col_feat1:
#         st.markdown("""
#         <div style="background: white; padding: 25px; border-radius: 12px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; height: 180px;">
#             <div style="font-size: 2rem; margin-bottom: 10px;">🎯</div>
#             <h3 style="color: #1e40af; font-size: 1.1rem; margin-bottom: 10px; font-weight: 600;">Structured Assessment</h3>
#             <p style="color: #64748b; font-size: 0.9rem; line-height: 1.5;">Standardized evaluation process with consistent criteria</p>
#         </div>
#         """, unsafe_allow_html=True)
    
#     with col_feat2:
#         st.markdown("""
#         <div style="background: white; padding: 25px; border-radius: 12px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; height: 180px;">
#             <div style="font-size: 2rem; margin-bottom: 10px;">📊</div>
#             <h3 style="color: #1e40af; font-size: 1.1rem; margin-bottom: 10px; font-weight: 600;">Detailed Analytics</h3>
#             <p style="color: #64748b; font-size: 0.9rem; line-height: 1.5;">Comprehensive metrics including fluency, accuracy, and confidence</p>
#         </div>
#         """, unsafe_allow_html=True)
    
#     with col_feat3:
#         st.markdown("""
#         <div style="background: white; padding: 25px; border-radius: 12px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; height: 180px;">
#             <div style="font-size: 2rem; margin-bottom: 10px;">✅</div>
#             <h3 style="color: #1e40af; font-size: 1.1rem; margin-bottom: 10px; font-weight: 600;">Compliance Monitoring</h3>
#             <p style="color: #64748b; font-size: 0.9rem; line-height: 1.5;">Real-time monitoring ensures assessment integrity</p>
#         </div>
#         """, unsafe_allow_html=True)
    
#     st.markdown("<br>", unsafe_allow_html=True)
    
#     # Introduction
#     st.markdown("""
#     <div class="guideline-box">
#         <h2 style="font-size: 1.3rem; margin-bottom: 15px;">📋 Before You Begin</h2>
#         <p style="font-size: 1rem; line-height: 1.7; color: #475569;">
#             This platform evaluates candidates through structured video interviews. Please carefully review 
#             the camera positioning requirements and technical specifications outlined below to ensure a smooth 
#             assessment experience.
#         </p>
#     </div>
#     """, unsafe_allow_html=True)
    
#     # Frame Positioning Guidelines
#     st.markdown("""
#     <h2 style="font-size: 1.3rem; color: #1e40af; margin: 30px 0 20px 0; font-weight: 600;">
#         📹 Camera Positioning Requirements
#     </h2>
#     """, unsafe_allow_html=True)
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.markdown("""
#         <div style="background: #f0fdf4; padding: 20px; border-radius: 10px; border: 2px solid #22c55e; height: 100%;">
#             <h4 style="color: #166534; font-size: 1.05rem; margin-bottom: 15px; font-weight: 600;">✅ Correct Positioning</h4>
#         """, unsafe_allow_html=True)
#         correct_img = create_frame_demo_image(is_correct=True)
#         st.image(correct_img, width='stretch')
#         st.markdown("""
#             <div style="margin-top: 15px;">
#                 <p style="color: #166534; margin: 8px 0; font-size: 0.95rem;"><strong>✓</strong> Center yourself in the frame</p>
#                 <p style="color: #166534; margin: 8px 0; font-size: 0.95rem;"><strong>✓</strong> Keep entire face visible within boundaries</p>
#                 <p style="color: #166534; margin: 8px 0; font-size: 0.95rem;"><strong>✓</strong> Remain alone in the frame</p>
#                 <p style="color: #166534; margin: 8px 0; font-size: 0.95rem;"><strong>✓</strong> Ensure adequate lighting</p>
#                 <p style="color: #166534; margin: 8px 0; font-size: 0.95rem;"><strong>✓</strong> Maintain forward gaze</p>
#             </div>
#         </div>
#         """, unsafe_allow_html=True)
    
#     with col2:
#         st.markdown("""
#         <div style="background: #fef2f2; padding: 20px; border-radius: 10px; border: 2px solid #ef4444; height: 100%;">
#             <h4 style="color: #991b1b; font-size: 1.05rem; margin-bottom: 15px; font-weight: 600;">❌ Common Mistakes</h4>
#         """, unsafe_allow_html=True)
#         incorrect_img = create_frame_demo_image(is_correct=False)
#         st.image(incorrect_img, width='stretch')
#         st.markdown("""
#             <div style="margin-top: 15px;">
#                 <p style="color: #991b1b; margin: 8px 0; font-size: 0.95rem;"><strong>✗</strong> Moving outside frame boundaries</p>
#                 <p style="color: #991b1b; margin: 8px 0; font-size: 0.95rem;"><strong>✗</strong> Multiple people visible</p>
#                 <p style="color: #991b1b; margin: 8px 0; font-size: 0.95rem;"><strong>✗</strong> Obstructed or partial view</p>
#                 <p style="color: #991b1b; margin: 8px 0; font-size: 0.95rem;"><strong>✗</strong> Poor lighting conditions</p>
#                 <p style="color: #991b1b; margin: 8px 0; font-size: 0.95rem;"><strong>✗</strong> Extended periods looking away</p>
#             </div>
#         </div>
#         """, unsafe_allow_html=True)
    
#     # Assessment Process
#     st.markdown("""
#     <h2 style="font-size: 1.3rem; color: #1e40af; margin: 30px 0 20px 0; font-weight: 600;">
#         📝 Assessment Process
#     </h2>
#     <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 2px 4px rgba(0,0,0,0.06); border: 1px solid #e2e8f0;">
#         <ol style="font-size: 1rem; line-height: 2; color: #475569; padding-left: 20px;">
#             <li><strong style="color: #1e40af;">Initial Setup (60 seconds):</strong> Position yourself within the marked boundaries and adjust lighting</li>
#             <li><strong style="color: #1e40af;">Environment Scan:</strong> System records baseline environment to detect any changes</li>
#             <li><strong style="color: #1e40af;">Interview Session:</strong> Respond to {} questions (20 seconds per question)</li>
#             <li><strong style="color: #1e40af;">Continuous Monitoring:</strong> System monitors compliance throughout the session</li>
#             <li><strong style="color: #1e40af;">Results Analysis:</strong> Receive comprehensive evaluation with detailed feedback</li>
#         </ol>
#     </div>
#     """.format(len(QUESTIONS)), unsafe_allow_html=True)
    
#     # Technical Requirements
#     st.markdown("""
#     <h2 style="font-size: 1.3rem; color: #1e40af; margin: 30px 0 20px 0; font-weight: 600;">
#         💻 Technical Requirements
#     </h2>
#     """, unsafe_allow_html=True)
    
#     col_tech1, col_tech2 = st.columns(2)
    
#     with col_tech1:
#         st.markdown("""
#         <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 2px 4px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; height: 100%;">
#             <h3 style="color: #1e40af; font-size: 1.05rem; margin-bottom: 15px; font-weight: 600;">Hardware Requirements</h3>
#             <ul style="color: #475569; font-size: 0.95rem; line-height: 1.8; padding-left: 20px;">
#                 <li>Functional webcam (minimum 720p recommended)</li>
#                 <li>Clear microphone with noise cancellation</li>
#                 <li>Stable internet connection (minimum 5 Mbps)</li>
#                 <li>Desktop or laptop computer (tablets not recommended)</li>
#             </ul>
#         </div>
#         """, unsafe_allow_html=True)
    
#     with col_tech2:
#         st.markdown("""
#         <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 2px 4px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; height: 100%;">
#             <h3 style="color: #1e40af; font-size: 1.05rem; margin-bottom: 15px; font-weight: 600;">Environment Setup</h3>
#             <ul style="color: #475569; font-size: 0.95rem; line-height: 1.8; padding-left: 20px;">
#                 <li>Quiet, private space without interruptions</li>
#                 <li>Consistent front-facing lighting (avoid backlighting)</li>
#                 <li>Neutral, uncluttered background</li>
#                 <li>Comfortable seating with good posture support</li>
#             </ul>
#         </div>
#         """, unsafe_allow_html=True)
    
#     # Confirmation
#     st.markdown("""
#     <h2 style="font-size: 1.3rem; color: #1e40af; margin: 30px 0 20px 0; font-weight: 600;">
#         ✅ Ready to Begin
#     </h2>
#     """, unsafe_allow_html=True)
    
#     if 'guidelines_accepted' not in st.session_state:
#         st.session_state.guidelines_accepted = False
    
#     # Styled checkbox
#     st.markdown("""
#     <div style="background: white; padding: 20px; border-radius: 12px; box-shadow: 0 2px 4px rgba(0,0,0,0.06); border: 1px solid #e2e8f0;">
#     """, unsafe_allow_html=True)
    
#     st.session_state.guidelines_accepted = st.checkbox(
#         f"I confirm that I have reviewed all guidelines and am prepared to complete {len(QUESTIONS)} interview questions under the specified conditions.",
#         value=st.session_state.guidelines_accepted,
#         key="guidelines_checkbox"
#     )
    
#     st.markdown("</div>", unsafe_allow_html=True)
    
#     st.markdown("<br>", unsafe_allow_html=True)
    
#     # Proceed Button
#     if st.session_state.guidelines_accepted:
#         st.markdown("""
#         <div style="background: #f0fdf4; padding: 20px; border-radius: 12px; border-left: 4px solid #22c55e; margin: 20px 0;">
#             <p style="color: #166534; margin: 0; font-size: 1rem; font-weight: 500;">
#                 ✅ You are ready to proceed with the assessment.
#             </p>
#         </div>
#         """, unsafe_allow_html=True)
        
#         col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
#         with col_btn2:
#             if st.button("🚀 Begin Assessment", type="primary", width='stretch', key="begin_btn"):
#                 st.session_state.page = "interview"
#                 st.session_state.interview_started = False
#                 st.rerun()
#     else:
#         st.markdown("""
#         <div style="background: #eff6ff; padding: 20px; border-radius: 12px; border-left: 4px solid #3b82f6; margin: 20px 0;">
#             <p style="color: #1e40af; margin: 0; font-size: 1rem;">
#                 ℹ️ Please confirm that you have reviewed the guidelines to continue.
#             </p>
#         </div>
#         """, unsafe_allow_html=True)

# # ==================== LOAD MODELS ====================
# @st.cache_resource(show_spinner="Initializing assessment system...")
# def load_all_models():
#     """Load all AI models and return dictionary - CACHED to prevent reloading"""
#     models = {}
    
#     # Face model for emotion
#     if DEEPFACE_AVAILABLE:
#         try:
#             _ = DeepFace.build_model("Facenet")
#             models['face_loaded'] = True
#         except:
#             models['face_loaded'] = False
#     else:
#         models['face_loaded'] = False
    
#     # Sentence transformer
#     if SENTENCE_TRANSFORMER_AVAILABLE:
#         try:
#             models['sentence_model'] = SentenceTransformer('all-MiniLM-L6-v2')
#         except:
#             models['sentence_model'] = None
#     else:
#         models['sentence_model'] = None
    
#     # MediaPipe
#     if MP_AVAILABLE:
#         try:
#             models['face_mesh'] = mp_face_mesh.FaceMesh(
#                 static_image_mode=False,
#                 max_num_faces=5,
#                 refine_landmarks=True,
#                 min_detection_confidence=0.5,
#                 min_tracking_confidence=0.5
#             )
#             models['hands'] = mp_hands.Hands(
#                 static_image_mode=False,
#                 max_num_hands=2,
#                 min_detection_confidence=0.5,
#                 min_tracking_confidence=0.5
#             )
#         except:
#             models['face_mesh'] = None
#             models['hands'] = None
#     else:
#         models['face_mesh'] = None
#         models['hands'] = None
    
#     # YOLO
#     if YOLO_AVAILABLE:
#         try:
#             models['yolo'] = YOLO("yolov8n.pt")
#             models['yolo_cls'] = YOLO("yolov8n-cls.pt")
#         except:
#             models['yolo'] = None
#             models['yolo_cls'] = None
#     else:
#         models['yolo'] = None
#         models['yolo_cls'] = None
    
#     return models

# # Load models once and cache
# models = load_all_models()

# # ==================== INITIALIZE SYSTEMS ====================
# recording_system = RecordingSystem(models)
# analysis_system = AnalysisSystem(models)
# scoring_dashboard = ScoringDashboard()

# # ==================== SESSION STATE ====================
# if "page" not in st.session_state:
#     st.session_state.page = "home"
# if "results" not in st.session_state:
#     st.session_state.results = []
# if "interview_started" not in st.session_state:
#     st.session_state.interview_started = False
# if "interview_complete" not in st.session_state:
#     st.session_state.interview_complete = False

# # ==================== MAIN ROUTING ====================
# if st.session_state.page == "home":
#     show_home_page()

# else:  # Interview page
#     st.markdown('<div class="main-title">Interview Assessment Session</div>', unsafe_allow_html=True)
#     st.markdown('<div class="subtext">Complete all questions to receive your evaluation</div>', unsafe_allow_html=True)
    
#     # Navigation (minimal, no sidebar)
#     if not st.session_state.interview_complete:
#         col_nav1, col_nav2, col_nav3 = st.columns([1, 3, 1])
#         with col_nav1:
#             if st.button("← Home", use_container_width=True):
#                 st.session_state.page = "home"
#                 st.session_state.interview_started = False
#                 st.session_state.interview_complete = False
#                 st.rerun()
#     else:
#         col_nav1, col_nav2 = st.columns([1, 1])
#         with col_nav1:
#             if st.button("← Home", use_container_width=True):
#                 st.session_state.page = "home"
#                 st.session_state.interview_started = False
#                 st.session_state.interview_complete = False
#                 st.rerun()
#         with col_nav2:
#             if st.button("🔄 New Assessment", use_container_width=True):
#                 st.session_state.results = []
#                 st.session_state.interview_started = False
#                 st.session_state.interview_complete = False
#                 st.rerun()
    
#     # ==================== MAIN CONTENT ====================
    
#     if not st.session_state.interview_started and not st.session_state.interview_complete:
#         # Show start button
#         st.markdown("---")
#         st.markdown("""
#         <div class="guideline-box">
#             <h2 style="text-align: center;">Ready to Begin?</h2>
#             <p style="font-size: 1rem; text-align: center; line-height: 1.6;">
#                 You will respond to <strong>{}</strong> questions.<br>
#                 Each question allows <strong>20 seconds</strong> for your response.<br>
#                 The system will monitor compliance throughout the session.
#             </p>
#         </div>
#         """.format(len(QUESTIONS)), unsafe_allow_html=True)
        
#         col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
#         with col_btn2:
#             if st.button("🚀 Begin Assessment", type="primary", width='stretch', key="start_btn_interview"):
#                 st.session_state.interview_started = True
#                 st.rerun()
    
#     elif st.session_state.interview_started and not st.session_state.interview_complete:
#         # LAYOUT: QUESTION (LEFT) | VIDEO (RIGHT)
#         st.markdown("---")
        
#         col_question, col_video = st.columns([2, 3])
        
#         with col_question:
#             question_placeholder = st.empty()
        
#         with col_video:
#             st.markdown('<div class="video-container">', unsafe_allow_html=True)
#             video_placeholder = st.empty()
#             st.markdown('</div>', unsafe_allow_html=True)
        
#         # Status area
#         st.markdown("---")
#         countdown_placeholder = st.empty()
#         status_placeholder = st.empty()
#         progress_bar = st.progress(0)
#         timer_text = st.empty()
        
#         # UI Callbacks
#         ui_callbacks = {
#             'countdown_update': lambda msg: countdown_placeholder.warning(msg) if msg else countdown_placeholder.empty(),
#             'video_update': lambda frame: video_placeholder.image(frame, channels="BGR", use_container_width=True) if frame is not None else video_placeholder.empty(),
#             'status_update': lambda text: status_placeholder.markdown(text) if text else status_placeholder.empty(),
#             'progress_update': lambda val: progress_bar.progress(val),
#             'timer_update': lambda text: timer_text.info(text) if text else timer_text.empty(),
#             'question_update': lambda q_num, q_text, q_tip="": question_placeholder.markdown(
#                 f'''<div class="question-box">
#                     <h2>Question {q_num} of {len(QUESTIONS)}</h2>
#                     <div class="question-text">{q_text}</div>
#                     <div class="question-meta">
#                         💡 <strong>Guidance:</strong> {q_tip if q_tip else "Speak clearly and confidently"}
#                     </div>
#                 </div>''',
#                 unsafe_allow_html=True
#             ) if q_text else question_placeholder.empty()
#         }
        
#         # Run continuous interview
#         st.info("🎬 Initializing assessment session...")
#         session_result = recording_system.record_continuous_interview(
#             QUESTIONS, 
#             duration_per_question=20,
#             ui_callbacks=ui_callbacks
#         )
        
#         # Process results
#         if isinstance(session_result, dict) and 'questions_results' in session_result:
#             st.session_state.results = []
            
#             for q_result in session_result['questions_results']:
#                 question_data = QUESTIONS[q_result['question_number'] - 1]
                
#                 # Analyze each question
#                 analysis_results = analysis_system.analyze_recording(q_result, question_data, 20)
                
#                 # Build result dict
#                 result = {
#                     "question": question_data["question"],
#                     "video_path": session_result.get('session_video_path', ''),
#                     "audio_path": q_result.get('audio_path', ''),
#                     "transcript": q_result.get('transcript', ''),
#                     "violations": q_result.get('violations', []),
#                     "violation_detected": q_result.get('violation_detected', False),
#                     "fused_emotions": analysis_results.get('fused_emotions', {}),
#                     "emotion_scores": analysis_results.get('emotion_scores', {}),
#                     "accuracy": analysis_results.get('accuracy', 0),
#                     "fluency": analysis_results.get('fluency', 0),
#                     "wpm": analysis_results.get('wpm', 0),
#                     "blink_count": q_result.get('blink_count', 0),
#                     "outfit": analysis_results.get('outfit', 'Unknown'),
#                     "has_valid_data": analysis_results.get('has_valid_data', False),
#                     "fluency_detailed": analysis_results.get('fluency_detailed', {}),
#                     "fluency_level": analysis_results.get('fluency_level', 'No Data'),
#                     "grammar_errors": analysis_results.get('grammar_errors', 0),
#                     "filler_count": analysis_results.get('filler_count', 0),
#                     "filler_ratio": analysis_results.get('filler_ratio', 0),
#                     "improvements_applied": analysis_results.get('improvements_applied', {})
#                 }
                
#                 # Make hiring decision
#                 decision, reasons = scoring_dashboard.decide_hire(result)
#                 result["hire_decision"] = decision
#                 result["hire_reasons"] = reasons
                
#                 st.session_state.results.append(result)
            
#             st.session_state.interview_complete = True
            
#             # Show completion message
#             total_violations = session_result.get('total_violations', 0)
#             if total_violations > 0:
#                 st.warning(f"⚠️ Assessment completed with {total_violations} compliance issue(s) detected.")
#             else:
#                 st.success("🎉 Assessment completed successfully!")
            
#             import time
#             time.sleep(2)
#             st.rerun()
#         else:
#             st.error("❌ Assessment failed. Please try again.")
#             st.session_state.interview_started = False
    
#     else:
#         # Show results dashboard
#         st.markdown("---")
#         scoring_dashboard.render_dashboard(st.session_state.results)
    
#     # ==================== FOOTER ====================
#     st.markdown("---")
#     st.markdown(
#         "<div style='text-align: center; color: #94a3b8; padding: 20px; font-size: 0.85rem;'>"
#         "Interview Assessment Platform | Professional Evaluation System"
#         "</div>",
#         unsafe_allow_html=True
#     )




"""
Main Integration File - AI Interview System
SIMPLIFIED, PROFESSIONAL UI - Normal Website Look
"""

import streamlit as st
import warnings
import os
from PIL import Image, ImageDraw

# Import the three modular systems
from Recording_system import RecordingSystem
from analysis_system import AnalysisSystem
from scoring_dashboard import ScoringDashboard

warnings.filterwarnings('ignore')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Try importing optional modules
try:
    import mediapipe as mp
    MP_AVAILABLE = True
    mp_face_mesh = mp.solutions.face_mesh
    mp_hands = mp.solutions.hands
except:
    MP_AVAILABLE = False

try:
    from ultralytics import YOLO
    YOLO_AVAILABLE = True
except:
    YOLO_AVAILABLE = False

try:
    from sentence_transformers import SentenceTransformer
    SENTENCE_TRANSFORMER_AVAILABLE = True
except:
    SENTENCE_TRANSFORMER_AVAILABLE = False

try:
    from deepface import DeepFace
    DEEPFACE_AVAILABLE = True
except:
    DEEPFACE_AVAILABLE = False

# ==================== PAGE CONFIG ====================
st.set_page_config(page_title="Interview Assessment Platform", layout="wide", page_icon="🎯")

# ==================== SIMPLE, CLEAN STYLES ====================
st.markdown("""
<style>
/* Hide Streamlit branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Simple body styling */
body { 
    background-color: #ffffff; 
    color: #333333; 
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
}

/* Simple headers */
h1 { 
    color: #2c3e50; 
    font-weight: 600;
    margin-bottom: 0.5rem;
}

h2 { 
    color: #34495e; 
    font-weight: 500;
    margin-top: 1.5rem;
    margin-bottom: 0.75rem;
}

h3 { 
    color: #555555; 
    font-weight: 500;
}

/* Simple boxes */
.info-box {
    background: #f8f9fa;
    border: 1px solid #dee2e6;
    border-radius: 4px;
    padding: 1rem;
    margin: 1rem 0;
}

.success-box {
    background: #d4edda;
    border: 1px solid #c3e6cb;
    border-left: 4px solid #28a745;
    border-radius: 4px;
    padding: 1rem;
    margin: 1rem 0;
}

.warning-box {
    background: #fff3cd;
    border: 1px solid #ffeaa7;
    border-left: 4px solid #ffc107;
    border-radius: 4px;
    padding: 1rem;
    margin: 1rem 0;
}

.error-box {
    background: #f8d7da;
    border: 1px solid #f5c6cb;
    border-left: 4px solid #dc3545;
    border-radius: 4px;
    padding: 1rem;
    margin: 1rem 0;
}

/* Simple question box */
.question-box {
    background: #ffffff;
    border: 1px solid #dee2e6;
    border-radius: 4px;
    padding: 1.5rem;
    margin-bottom: 1rem;
    min-height: 200px;
}

.question-box h3 {
    color: #2c3e50;
    margin-bottom: 1rem;
    padding-bottom: 0.75rem;
    border-bottom: 1px solid #e9ecef;
}

/* Simple metric cards */
.metric-card {
    background: #ffffff;
    border: 1px solid #dee2e6;
    border-radius: 4px;
    padding: 1rem;
    text-align: center;
    margin-bottom: 0.5rem;
}

.metric-card h3 {
    color: #2c3e50;
    font-size: 1.5rem;
    margin: 0;
}

.metric-card p {
    color: #6c757d;
    font-size: 0.875rem;
    margin: 0.25rem 0 0 0;
}

/* Hide sidebar */
[data-testid="stSidebar"] {
    display: none;
}

/* Simple buttons */
.stButton > button {
    border-radius: 4px;
    border: 1px solid #dee2e6;
}

/* Simple progress bar */
.stProgress > div > div {
    background-color: #007bff;
}
</style>
""", unsafe_allow_html=True)

# ==================== QUESTIONS CONFIGURATION ====================
QUESTIONS = [
    {
        "question": "Tell me about yourself.",
        "type": "personal",
        "ideal_answer": "I'm a computer science postgraduate with a strong interest in AI and software development. I've worked on several projects involving Python, machine learning, and data analysis, which helped me improve both my technical and problem-solving skills. I enjoy learning new technologies and applying them to create practical solutions. Outside of academics, I like collaborating on team projects and continuously developing my professional skills.",
        "tip": "Focus on your background, skills, and personality"
    },
    {
        "question": "What are your strengths and weaknesses?",
        "type": "personal",
        "ideal_answer": "One of my key strengths is that I'm very detail-oriented and persistent – I make sure my work is accurate and well-tested. I also enjoy solving complex problems and learning new tools quickly. As for weaknesses, I used to spend too much time perfecting small details, which sometimes slowed me down. But I've been improving by prioritizing tasks better and focusing on overall impact.",
        "tip": "Be honest and show self-awareness"
    },
    {
        "question": "Where do you see yourself in the next 5 years?",
        "type": "personal",
        "ideal_answer": "In the next five years, I see myself growing into a more responsible and skilled professional, ideally in a role where I can contribute to meaningful projects involving AI and software development. I'd also like to take on leadership responsibilities and guide new team members as I gain experience.",
        "tip": "Show ambition aligned with career growth"
    }
]

# ==================== GENERATE DEMO IMAGES ====================
def create_frame_demo_image(is_correct=True):
    """Create demonstration image showing correct/incorrect positioning"""
    width, height = 500, 350
    img = Image.new('RGB', (width, height), color='#f8f9fa')
    draw = ImageDraw.Draw(img)
    
    margin = 40
    boundary_color = '#28a745' if is_correct else '#dc3545'
    
    # Draw boundaries
    draw.rectangle([margin, margin, width-margin, height-margin], outline=boundary_color, width=3)
    
    if is_correct:
        # Draw person inside
        head_x, head_y = width // 2, margin + 60
        draw.ellipse([head_x - 30, head_y - 30, head_x + 30, head_y + 30], fill='#ffc107', outline='#333333', width=2)
        
        body_y = head_y + 40
        draw.rectangle([head_x - 40, body_y, head_x + 40, body_y + 80], fill='#007bff', outline='#333333', width=2)
        
        draw.text((width//2 - 80, height - 30), "✓ Correct Position", fill='#28a745')
    else:
        # Draw person outside
        head_x, head_y = margin - 20, margin + 60
        draw.ellipse([head_x - 30, head_y - 30, head_x + 30, head_y + 30], fill='#ffc107', outline='#333333', width=2)
        
        draw.text((width//2 - 80, height - 30), "✗ Outside Bounds", fill='#dc3545')
    
    return img

# ==================== HOME PAGE ====================
def show_home_page():
    """Display clean home page"""
    
    st.title("Interview Assessment Platform")
    st.write("Professional evaluation system for video interviews")
    
    st.markdown("---")
    
    # Simple features
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **📋 Structured Assessment**
        
        Standardized evaluation with consistent criteria
        """)
    
    with col2:
        st.markdown("""
        **📊 Detailed Analytics**
        
        Comprehensive metrics and performance insights
        """)
    
    with col3:
        st.markdown("""
        **✅ Compliance Monitoring**
        
        Real-time monitoring ensures integrity
        """)
    
    st.markdown("---")
    
    # Introduction
    st.subheader("Before You Begin")
    st.write("""
    This platform evaluates candidates through structured video interviews. Please review 
    the camera positioning requirements below to ensure a smooth assessment.
    """)
    
    # Frame positioning
    st.subheader("Camera Positioning Requirements")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**✅ Correct Positioning**")
        correct_img = create_frame_demo_image(is_correct=True)
        st.image(correct_img, use_container_width=True)
        st.markdown("""
        - Center yourself in the frame
        - Keep entire face visible
        - Remain alone in the frame
        - Ensure adequate lighting
        - Maintain forward gaze
        """)
    
    with col2:
        st.markdown("**❌ Common Mistakes**")
        incorrect_img = create_frame_demo_image(is_correct=False)
        st.image(incorrect_img, use_container_width=True)
        st.markdown("""
        - Moving outside boundaries
        - Multiple people visible
        - Obstructed or partial view
        - Poor lighting conditions
        - Extended periods looking away
        """)
    
    st.markdown("---")
    
    # Assessment process
    st.subheader("Assessment Process")
    st.markdown(f"""
    1. **Initial Setup (60 seconds):** Position yourself within marked boundaries
    2. **Environment Scan:** System records baseline to detect changes
    3. **Interview Session:** Respond to {len(QUESTIONS)} questions (20 seconds each)
    4. **Continuous Monitoring:** System monitors compliance throughout
    5. **Results Analysis:** Receive comprehensive evaluation with feedback
    """)
    
    st.markdown("---")
    
    # Technical requirements
    st.subheader("Technical Requirements")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Hardware**
        - Functional webcam (720p recommended)
        - Clear microphone
        - Stable internet (5 Mbps minimum)
        - Desktop or laptop computer
        """)
    
    with col2:
        st.markdown("""
        **Environment**
        - Quiet, private space
        - Front-facing lighting
        - Neutral background
        - Comfortable seating
        """)
    
    st.markdown("---")
    
    # Confirmation
    st.subheader("Ready to Begin")
    
    if 'guidelines_accepted' not in st.session_state:
        st.session_state.guidelines_accepted = False
    
    st.session_state.guidelines_accepted = st.checkbox(
        f"I confirm that I have reviewed all guidelines and am prepared to complete {len(QUESTIONS)} interview questions.",
        value=st.session_state.guidelines_accepted,
        key="guidelines_checkbox"
    )
    
    if st.session_state.guidelines_accepted:
        st.success("✅ You are ready to proceed with the assessment.")
        if st.button("Begin Assessment", type="primary"):
            st.session_state.page = "interview"
            st.session_state.interview_started = False
            st.rerun()
    else:
        st.info("ℹ️ Please confirm that you have reviewed the guidelines to continue.")

# ==================== LOAD MODELS ====================
@st.cache_resource(show_spinner="Initializing assessment system...")
def load_all_models():
    """Load all AI models and return dictionary"""
    models = {}
    
    if DEEPFACE_AVAILABLE:
        try:
            _ = DeepFace.build_model("Facenet")
            models['face_loaded'] = True
        except:
            models['face_loaded'] = False
    else:
        models['face_loaded'] = False
    
    if SENTENCE_TRANSFORMER_AVAILABLE:
        try:
            models['sentence_model'] = SentenceTransformer('all-MiniLM-L6-v2')
        except:
            models['sentence_model'] = None
    else:
        models['sentence_model'] = None
    
    if MP_AVAILABLE:
        try:
            models['face_mesh'] = mp_face_mesh.FaceMesh(
                static_image_mode=False,
                max_num_faces=5,
                refine_landmarks=True,
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5
            )
            models['hands'] = mp_hands.Hands(
                static_image_mode=False,
                max_num_hands=2,
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5
            )
        except:
            models['face_mesh'] = None
            models['hands'] = None
    else:
        models['face_mesh'] = None
        models['hands'] = None
    
    if YOLO_AVAILABLE:
        try:
            models['yolo'] = YOLO("yolov8n.pt")
            models['yolo_cls'] = YOLO("yolov8n-cls.pt")
        except:
            models['yolo'] = None
            models['yolo_cls'] = None
    else:
        models['yolo'] = None
        models['yolo_cls'] = None
    
    return models

models = load_all_models()

# ==================== INITIALIZE SYSTEMS ====================
recording_system = RecordingSystem(models)
analysis_system = AnalysisSystem(models)
scoring_dashboard = ScoringDashboard()

# ==================== SESSION STATE ====================
if "page" not in st.session_state:
    st.session_state.page = "home"
if "results" not in st.session_state:
    st.session_state.results = []
if "interview_started" not in st.session_state:
    st.session_state.interview_started = False
if "interview_complete" not in st.session_state:
    st.session_state.interview_complete = False

# ==================== MAIN ROUTING ====================
if st.session_state.page == "home":
    show_home_page()

else:  # Interview page
    st.title("Interview Assessment Session")
    st.write("Complete all questions to receive your evaluation")
    
    # Simple navigation
    if not st.session_state.interview_complete:
        if st.button("← Back to Home"):
            st.session_state.page = "home"
            st.session_state.interview_started = False
            st.session_state.interview_complete = False
            st.rerun()
    else:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("← Back to Home"):
                st.session_state.page = "home"
                st.session_state.interview_started = False
                st.session_state.interview_complete = False
                st.rerun()
        with col2:
            if st.button("🔄 New Assessment"):
                st.session_state.results = []
                st.session_state.interview_started = False
                st.session_state.interview_complete = False
                st.rerun()
    
    st.markdown("---")
    
    # ==================== MAIN CONTENT ====================
    
    if not st.session_state.interview_started and not st.session_state.interview_complete:
        st.subheader("Ready to Begin?")
        st.write(f"""
        - You will respond to **{len(QUESTIONS)} questions**
        - Each question allows **20 seconds** for your response
        - The system will monitor compliance throughout
        """)
        
        if st.button("Begin Assessment", type="primary"):
            st.session_state.interview_started = True
            st.rerun()
    
    elif st.session_state.interview_started and not st.session_state.interview_complete:
        col_question, col_video = st.columns([2, 3])
        
        with col_question:
            question_placeholder = st.empty()
        
        with col_video:
            video_placeholder = st.empty()
        
        st.markdown("---")
        countdown_placeholder = st.empty()
        status_placeholder = st.empty()
        progress_bar = st.progress(0)
        timer_text = st.empty()
        
        ui_callbacks = {
            'countdown_update': lambda msg: countdown_placeholder.warning(msg) if msg else countdown_placeholder.empty(),
            'video_update': lambda frame: video_placeholder.image(frame, channels="BGR", use_container_width=True) if frame is not None else video_placeholder.empty(),
            'status_update': lambda text: status_placeholder.markdown(text) if text else status_placeholder.empty(),
            'progress_update': lambda val: progress_bar.progress(val),
            'timer_update': lambda text: timer_text.info(text) if text else timer_text.empty(),
            'question_update': lambda q_num, q_text, q_tip="": question_placeholder.markdown(
                f'''<div class="question-box">
                    <h3>Question {q_num} of {len(QUESTIONS)}</h3>
                    <p style="font-size: 1.1rem; margin: 1rem 0;">{q_text}</p>
                    <p style="color: #6c757d; font-size: 0.9rem; margin-top: 1rem;">
                        💡 <strong>Tip:</strong> {q_tip if q_tip else "Speak clearly and confidently"}
                    </p>
                </div>''',
                unsafe_allow_html=True
            ) if q_text else question_placeholder.empty()
        }
        
        st.info("🎬 Initializing assessment session...")
        session_result = recording_system.record_continuous_interview(
            QUESTIONS, 
            duration_per_question=20,
            ui_callbacks=ui_callbacks
        )
        
        if isinstance(session_result, dict) and 'questions_results' in session_result:
            st.session_state.results = []
            
            for q_result in session_result['questions_results']:
                question_data = QUESTIONS[q_result['question_number'] - 1]
                analysis_results = analysis_system.analyze_recording(q_result, question_data, 20)
                
                result = {
                    "question": question_data["question"],
                    "video_path": session_result.get('session_video_path', ''),
                    "audio_path": q_result.get('audio_path', ''),
                    "transcript": q_result.get('transcript', ''),
                    "violations": q_result.get('violations', []),
                    "violation_detected": q_result.get('violation_detected', False),
                    "fused_emotions": analysis_results.get('fused_emotions', {}),
                    "emotion_scores": analysis_results.get('emotion_scores', {}),
                    "accuracy": analysis_results.get('accuracy', 0),
                    "fluency": analysis_results.get('fluency', 0),
                    "wpm": analysis_results.get('wpm', 0),
                    "blink_count": q_result.get('blink_count', 0),
                    "outfit": analysis_results.get('outfit', 'Unknown'),
                    "has_valid_data": analysis_results.get('has_valid_data', False),
                    "fluency_detailed": analysis_results.get('fluency_detailed', {}),
                    "fluency_level": analysis_results.get('fluency_level', 'No Data'),
                    "grammar_errors": analysis_results.get('grammar_errors', 0),
                    "filler_count": analysis_results.get('filler_count', 0),
                    "filler_ratio": analysis_results.get('filler_ratio', 0),
                    "improvements_applied": analysis_results.get('improvements_applied', {})
                }
                
                decision, reasons = scoring_dashboard.decide_hire(result)
                result["hire_decision"] = decision
                result["hire_reasons"] = reasons
                
                st.session_state.results.append(result)
            
            st.session_state.interview_complete = True
            
            total_violations = session_result.get('total_violations', 0)
            if total_violations > 0:
                st.warning(f"⚠️ Assessment completed with {total_violations} compliance issue(s).")
            else:
                st.success("🎉 Assessment completed successfully!")
            
            import time
            time.sleep(2)
            st.rerun()
        else:
            st.error("❌ Assessment failed. Please try again.")
            st.session_state.interview_started = False
    
    else:
        scoring_dashboard.render_dashboard(st.session_state.results)