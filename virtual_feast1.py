import streamlit as st

st.set_page_config(layout="wide",page_title="Virtual Feast", page_icon="🍴")
# Set the background image
bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
background-image: url('https://mir-s3-cdn-cf.behance.net/project_modules/fs/4f5f9640211349.5776664fbfcf7.gif');
background-size: cover;
background-repeat: no-repeat;
}
</style>
'''
st.markdown(bg_img, unsafe_allow_html=True)
page_bg_img = '''
<style>
body {
    background-image: url("https://img.freepik.com/premium-photo/exquisite-indian-food-presentation-feast-eyes_729149-2331.jpg"); /* Replace with your image URL */
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    font-family: 'Arial', sans-serif;
    color: #333333;
}
.main .block-container {
    background-color: rgba(255, 255, 255, 0.8);
    padding: 2rem;
    border-radius: 15px;
    box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.2);
}
h1, h2, h3, h4, h5, h6 {
    color: #444444;
}
button {
    background-color: #4CAF50;
    border: none;
    color: white;
    padding: 10px 24px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 12px;
    transition: background-color 0.3s ease;
}
button:hover {
    background-color: #45a049;
}
</style>
'''

# Initialize session state for users and login status
if 'users' not in st.session_state:
    st.session_state['users'] = {}
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'current_user' not in st.session_state:
    st.session_state['current_user'] = None
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 'main'
if 'sub_page' not in st.session_state:
    st.session_state['sub_page'] = None

# Function to display login form
def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in st.session_state['users'] and st.session_state['users'][username] == password:
            st.session_state['logged_in'] = True
            st.session_state['current_user'] = username
            st.session_state['current_page'] = 'main'  # Reset to main page on login
            st.session_state['sub_page'] = None
            st.success(f"Logged in as {username}")
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")

# Function to display registration form
def register():
    st.title("Register")
    username = st.text_input("Choose a Username")
    password = st.text_input("Choose a Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    if st.button("Register"):
        if password == confirm_password:
            if username not in st.session_state['users']:
                st.session_state['users'][username] = password
                st.success("Registration successful! You can now login.")
            else:
                st.error("Username already exists")
        else:
            st.error("Passwords do not match")

# Function to display the main content after login
def main_page():
    st.title("WELCOME TO INDIAN FEAST!!!")
    st.write(f"You are logged in as {st.session_state['current_user']}!")
    
    st.markdown("""
        <style>
        .box-container {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-wrap: wrap;
        }
        .box {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 200px;
            width: 300px;
            margin: 20px;
            background-color: #f0f0f0;
            border: 2px solid #ccc;
            border-radius: 10px;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            color: white;
            transition: transform 0.3s ease, background-color 0.3s ease;
            cursor: pointer;
        }
        .box:hover {
            transform: scale(1.1);
        }
        .spices { background-color: #ff6347; }
        .desserts { background-color: #ffb6c1; }
        .south { background-color: #ffa07a; }
        .north { background-color: #cd5c5c; }
        /* Additional colors for Indian states */
        .tamilnadu { background-color: #87ceeb; }
        .kerala { background-color: #ffa500; }
        .andhra { background-color: #ff69b4; }
        .punjab { background-color: #9acd32; }
        .rajasthan { background-color: #ff69b4; }
        .karnataka { background-color: #9acd32; }
        .bengali { background-color: #ff69b4; }
        .maharashtra { background-color: #9acd32; }
        .sambar { background-color: #ff69b4; }
        .pongal { background-color: #9acd32; }
        .puttu { background-color: #ff69b4; }
        .thalassery { background-color: #9acd32; }
        .gutti { background-color: #ff69b4; }
        .biriyani { background-color: #9acd32; }
        .dosa { background-color: #ff69b4; }
        .bath { background-color: #9acd32; }
        .chole { background-color: #ff69b4; }
        .butter { background-color: #9acd32; }
        .kachori { background-color: #ff69b4; }
        .gulab { background-color: #ff69b4; }
        .ras { background-color: #9acd32; }
        .rasg { background-color: #ff69b4; }
        .soan { background-color: #9acd32; }
        .dal { background-color: #9acd32; }
        .box-button {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            all: unset;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100%;
            width: 100%;
            cursor: pointer;
        }
        </style>
    """, unsafe_allow_html=True)

    if st.button("Logout"):
            st.session_state['logged_in'] = False
            st.session_state['current_user'] = None
            st.experimental_rerun()
    st.subheader("Explore Our Menu")
    if st.session_state['current_page'] == 'main':
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Spices"):
                st.session_state['current_page'] = 'spices'
                st.session_state['sub_page'] = None
                st.experimental_rerun()
            st.markdown('<div class="box spices">Spices</div>', unsafe_allow_html=True)
        with col2:
            if st.button("Desserts"):
                st.session_state['current_page'] = 'desserts'
                st.experimental_rerun()
            st.markdown('<div class="box desserts">Desserts</div>', unsafe_allow_html=True)
        st.markdown("---")
    elif st.session_state['current_page'] == 'desserts':
        st.subheader("Desserts Section!!\n PLEASE SCROLL DOWN TO SEE THE RECIPE ONCE YOU CLICK THE MENU")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Gulab Jamun"):
                st.session_state['sub_page'] = 'gulab_recipe'
                st.experimental_rerun()
            st.markdown('<div class="box gulab">Gulab Jamun</div>', unsafe_allow_html=True)
        with col2:
            if st.button("Rasmalai"):
                st.session_state['sub_page'] = 'ras_recipe'
                st.experimental_rerun()
            st.markdown('<div class="box ras">Rasmalai</div>', unsafe_allow_html=True)
        col3, col4 = st.columns(2)
        with col3:
            if st.button("Rasgulla"):
                st.session_state['sub_page'] = 'rasgulla_recipe'
                st.experimental_rerun()
            st.markdown('<div class="box rasg">Rasgulla</div>', unsafe_allow_html=True)
        with col4:
            if st.button("Soan Papdi"):
                st.session_state['sub_page'] = 'soan_recipe'
                st.experimental_rerun()
            st.markdown('<div class="box soan">Soan Papdi</div>', unsafe_allow_html=True)
            if st.button("Back to main page"):
                st.session_state['current_page'] = 'main'
                st.experimental_rerun()
        
        if st.session_state['sub_page'] == 'gulab_recipe':
            st.subheader("Gulab Jamun Recipe")

            gulab_recipe = """Instructions:\n
            For Sugar Syrup:\n
            1.	Prepare the Syrup: In a large pan, combine sugar and water. Heat the mixture, stirring occasionally, until the sugar dissolves. Bring it to a boil and let it simmer for 5-7 minutes until it slightly thickens.\n
            2.	Add Flavorings: Add cardamom powder, rose water, and saffron strands if using. Mix well and keep the syrup warm.\n
            For Gulab Jamun:\n
            1.	Prepare the Dough: In a mixing bowl, combine grated khoya, crumbled paneer, all-purpose flour, baking soda, and cardamom powder. Mix well.\n
            2.	Add Milk: Gradually add milk to the mixture and knead it into a smooth, soft dough. The dough should be pliable and not too sticky.\n
            3.	Shape the Dough: Divide the dough into small portions and roll them into smooth, crack-free balls. Ensure there are no cracks on the surface, as this will help them fry evenly.\n
            4.	Heat the Oil: Heat oil or ghee in a deep frying pan over medium-low heat. The oil should be hot but not smoking.\n
            5.	Fry the Balls: Gently slide the dough balls into the hot oil. Fry them on low heat, stirring gently to ensure even cooking, until they turn golden brown. This may take around 7-8 minutes.\n
            6.	Drain and Soak: Remove the fried gulab jamuns from the oil and drain them on paper towels to remove excess oil. Immediately transfer them to the warm sugar syrup.\n
            7.	Soak and Serve: Let the gulab jamuns soak in the syrup for at least 1-2 hours before serving. This allows them to absorb the syrup and become soft and juicy.\n
 """
            x_image = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ321oD8PPlAakIa_zqLt_kFeToBplXfCsMug&s"  # replace with your image URL or local path
            st.image(x_image, caption="Delicious Gulab Jamun")

            st.markdown(gulab_recipe)
        elif st.session_state['sub_page'] == 'ras_recipe':
            st.subheader("Rasmalai Recipe")

            ras_recipe = """Instructions:\n
            1.	Making Paneer:\n
        	Boil 1 liter of milk in a heavy-bottomed pan over medium heat. Stir occasionally to prevent it from sticking to the bottom.\n
        	Once the milk comes to a boil, reduce the heat and add lemon juice or vinegar gradually while stirring continuously. The milk will curdle, and the whey will separate.\n
        	Turn off the heat and let it sit for a minute. Then, strain the curdled milk through a muslin cloth or a fine sieve. Rinse the paneer under cold running water to remove any lemon or vinegar taste.\n
        	Squeeze out the excess water from the paneer and hang it or press it under a heavy object for about 30 minutes to remove any remaining whey.\n
            2.	Preparing Paneer Balls:\n
        	Knead the drained paneer for 5-7 minutes until it becomes smooth and soft.\n
        	Divide the paneer into small, equal-sized balls and flatten them slightly to form discs.\n
            3.	Cooking Paneer Balls:\n
        	In a large pan, bring 4 cups of water to a boil and add 1 cup of sugar. Stir until the sugar dissolves completely.\n
        	Gently add the paneer discs to the boiling syrup. Cover and cook on medium heat for 15-20 minutes until the paneer discs double in size.\n
        	Remove the pan from heat and let the paneer discs cool in the syrup. Once cooled, gently squeeze out the excess syrup from the paneer discs and set them aside.\n
            4.	Preparing Rabri:\n
        	In another heavy-bottomed pan, boil 1 liter of milk over medium heat. Reduce the heat and simmer until the milk thickens to about half its original volume. Stir frequently to prevent burning.\n
        	Add 1/2 cup of sugar, cardamom powder, saffron milk, and chopped nuts. Simmer for another 5-7 minutes until the sugar dissolves completely and the rabri is thick and creamy.\n
        	Add rose water or kewra water, if using, and mix well. Turn off the heat and let the rabri cool to room temperature.\n
            5.	Assembling Rasmalai:\n
        	Gently add the cooked paneer discs to the cooled rabri. Let them soak for at least 2-3 hours, or preferably overnight, in the refrigerator to absorb the flavors.\n
            6.	Serving:\n
        	Serve chilled Rasmalai, garnished with additional chopped nuts and a few saffron strands.\n"""
            y_image = "https://www.archanaskitchen.com/images/archanaskitchen/1-Author/moumita.malla-gmail.com/traditional_rasmalai_recipe.jpg"  # replace with your image URL or local path
            st.image(y_image, caption="Delicious Rasgula")

            st.markdown(ras_recipe)
        elif st.session_state['sub_page'] == 'rasgulla_recipe':
            st.subheader("Rasgulla Recipe")

            rasgulla_recipe = """Instructions:\n
            1.	Making Paneer:\n
        	    Bring the milk to a boil in a heavy-bottomed pan over medium heat.\n
                Once the milk comes to a boil, reduce the heat to low and gradually add the lemon juice or vinegar while stirring continuously. The milk will curdle, and the whey will separate.\n
            	Turn off the heat and let it sit for a minute. Then, strain the curdled milk through a muslin cloth or a fine sieve. Rinse the paneer under cold running water to remove any lemon or vinegar taste.\n
            	Squeeze out the excess water from the paneer and hang it or press it under a heavy object for about 30 minutes to remove any remaining whey.\n
            2.	Preparing Paneer Balls:\n
            	Knead the drained paneer for 5-7 minutes until it becomes smooth and soft. This step is crucial for achieving soft and spongy Rasgullas.\n
            	Divide the paneer into small, equal-sized portions and roll them into smooth balls with no cracks.\n
            3.	Preparing Sugar Syrup:\n
            	In a large, wide pan, combine the sugar and water. Bring it to a boil, stirring until the sugar dissolves completely.\n
            	Add the cardamom powder and rose water or kewra water, if using. Boil the syrup for a few minutes.\n
            4.	Cooking Paneer Balls:\n
            	Gently add the paneer balls to the boiling sugar syrup. Ensure that there is enough space in the pan for the balls to expand.\n
            	Cover the pan with a lid and cook on medium heat for about 15-20 minutes. The paneer balls will double in size as they cook. Make sure the syrup is boiling throughout the cooking process.\n
            	To ensure even cooking, you can gently shake the pan occasionally, but do not stir with a spoon as it can break the paneer balls.\n
            5.	Cooling and Serving:\n
            	Once cooked, remove the pan from heat and let the Rasgullas cool in the syrup to room temperature.\n
            	Transfer the Rasgullas along with the syrup to a serving bowl and refrigerate for a few hours before serving.\n
            6.	Serving:\n
            	Serve chilled Rasgullas as a dessert, garnished with a few saffron strands or a sprinkle of cardamom powder if desired.\n
                Enjoy your soft and spongy Rasgullas!
"""
            m_image = "https://5.imimg.com/data5/SELLER/Default/2023/8/338722324/UI/TQ/SX/38027562/white-sponge-rasgulla.png"  # replace with your image URL or local path
            st.image(m_image, caption="Delicious Rasgulla")

            st.markdown(rasgulla_recipe)
        elif st.session_state['sub_page'] == 'soan_recipe':
            st.subheader("Soan Recipe")

            soan_recipe = """ Instructions:\n
            1.	Prepare the Flour Mixture:\n
        	In a large bowl, mix the gram flour and all-purpose flour together.\n
        	Heat 1 cup of ghee in a pan and add the flour mixture. Roast on low heat until the mixture turns golden brown and gives a nice aroma. Stir continuously to avoid burning. Once done, set aside to cool.\n
            2.	Prepare the Sugar Syrup:\n
        	In another pan, combine sugar, water, and milk. Heat the mixture and let it come to a boil. Remove any impurities that float to the surface.\n
        	Continue to cook the syrup until it reaches the hard ball stage (around 120°C or 250°F). You can check this by dropping a small amount of syrup into cold water; it should form a hard ball.\n
            3.	Combine and Cook:\n
        	Once the syrup is ready, add cardamom powder and rose water (if using). Mix well.\n
        	Quickly pour the hot syrup into the roasted flour mixture. Mix thoroughly to ensure everything is well combined.\n
            4.	Shaping the Soan Papdi:\n
        	Transfer the mixture to a greased tray or plate. Spread it out evenly using a rolling pin or the back of a spoon.\n
        	Sprinkle the chopped nuts on top and gently press them into the mixture.\n
            5.	Cutting and Cooling:\n
        	While the mixture is still warm, cut it into square or diamond shapes using a knife.\n
        	Allow the soan papdi to cool completely and set.\n
            6.	Serving:\n
        	Once cooled, separate the pieces and store them in an airtight container.\n

"""
            s_image = "https://c.ndtvimg.com/2019-10/hiovm7e8_soan-papdi_625x300_25_October_19.jpg?im=FeatureCrop,algorithm=dnn,width=384,height=384"  # replace with your image URL or local path
            st.image(s_image, caption="Delicious Soan Papdi")

            st.markdown(soan_recipe)
    elif st.session_state['current_page'] == 'spices':
        st.subheader("Spices")

        if st.session_state['sub_page'] is None:
            col1, col2 = st.columns(2)
            with col1:
                if st.button("South Indian"):
                    st.session_state['sub_page'] = 'south_indian'
                    st.experimental_rerun()
                st.markdown('<div class="box south">South Indian</div>', unsafe_allow_html=True)
            with col2:
                if st.button("North Indian"):
                    st.session_state['sub_page'] = 'north_indian'
                    st.experimental_rerun()
                st.markdown('<div class="box north">North Indian</div>', unsafe_allow_html=True)
                if st.button("Back to main page"):
                    st.session_state['current_page'] = 'main'
                    st.experimental_rerun()
        
        elif st.session_state['sub_page'] == 'south_indian':
            st.subheader("South Indian Section")

            col1, col2 = st.columns(2)
            with col1:
                if st.button("Tamil Nadu"):
                    st.session_state['sub_page'] = 'tamilnadu'
                    st.experimental_rerun()
                st.markdown('<div class="box tamilnadu">Tamil Nadu</div>', unsafe_allow_html=True)
                
                if st.button("Kerala"):
                    st.session_state['sub_page'] = 'kerala'
                    st.experimental_rerun()
                st.markdown('<div class="box kerala">Kerala</div>', unsafe_allow_html=True)

            with col2:
                if st.button("Andhra Pradesh"):
                    st.session_state['sub_page'] = 'andhra'
                    st.experimental_rerun()
                st.markdown('<div class="box andhra">Andhra Pradesh</div>', unsafe_allow_html=True)
                
                if st.button("Karnataka"):
                    st.session_state['sub_page'] = 'karnataka'
                    st.experimental_rerun()
                st.markdown('<div class="box karnataka">Karnataka</div>', unsafe_allow_html=True)
                if st.button("Back to spices"):
                    st.session_state['sub_page'] = None
                    st.experimental_rerun() 

        elif st.session_state['sub_page'] == 'north_indian':
            st.subheader("North Indian Section")

            col1, col2 = st.columns(2)
            with col1:
                if st.button("Punjab"):
                    st.session_state['sub_page'] = 'punjab'
                    st.experimental_rerun()
                st.markdown('<div class="box punjab">Punjab</div>', unsafe_allow_html=True)
            with col2:
                if st.button("Rajasthan"):
                    st.session_state['sub_page'] = 'rajasthan'
                    st.experimental_rerun()
                st.markdown('<div class="box rajasthan">Rajasthan</div>', unsafe_allow_html=True)
                if st.button("Back to india page"):
                    st.session_state['sub_page'] = None
                    st.experimental_rerun() 
        elif st.session_state['sub_page'] == 'punjab':
            st.subheader("Famous Dishes from Punjab")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Butter Chicken"):
                    st.session_state['sub_page'] = 'butter_recipe'
                    st.experimental_rerun()
                st.markdown('<div class="box butter">Butter Chicken</div>', unsafe_allow_html=True)
                if st.button("Chole Bhature"):
                    st.session_state['sub_page'] = 'chole_recipe'
                    st.experimental_rerun()
                st.markdown('<div class="box chole">Chole Bhature</div>', unsafe_allow_html=True)
                if st.button("Back"):
                    st.session_state['sub_page'] = 'north_indian'
                    st.experimental_rerun()
        elif st.session_state['sub_page'] == 'butter_recipe':
            st.subheader("Butter Chicken Recipe")

            butter_recipe = """Instructions:\n
            1.	Marinating the Chicken:\n
        	    In a large bowl, combine yogurt, ginger-garlic paste, red chili powder, turmeric powder, garam masala, salt, and lemon juice.\n
        	    Add the chicken pieces to the marinade, mix well, and let it marinate for at least 1 hour (preferably overnight in the refrigerator).\n
            2.	Cooking the Chicken:\n
        	    Heat a grill pan or a regular pan over medium heat. Add a little oil to grease the pan.\n
        	    Cook the marinated chicken pieces until they are browned and cooked through. You can also cook the chicken in an oven preheated to 200°C (400°F) for about 15-20 minutes.\n
        	    Set the cooked chicken pieces aside.\n
            3.	Making the Gravy:\n
        	    In a large pan or kadai, heat 3-4 tbsp butter and 1 tbsp oil over medium heat.\n
        	    Add finely chopped onions and slit green chilies. Sauté until the onions turn golden brown.\n
        	    Add ginger-garlic paste and sauté until the raw smell disappears.\n
        	    Add the tomato puree, turmeric powder, red chili powder, coriander powder, and cumin powder. Mix well and cook until the oil separates from the masala.\n
        	    Add salt to taste and mix well.\n
            4.	Blending the Gravy (Optional for a Smoother Texture):\n
        	    For a smoother gravy, you can blend the cooked onion-tomato mixture into a fine paste using a blender. Return the blended mixture to the pan.\n
            5.	Finishing the Gravy:\n
        	    Add the cooked chicken pieces to the gravy and mix well.\n
            	Add 1/2 cup of heavy cream and crushed kasuri methi. Mix well and let it simmer for 5-7 minutes on low heat.\n
            	Adjust the seasoning and consistency by adding water or cream as needed.\n
            6.	Garnishing and Serving:\n
            	Garnish with fresh cilantro leaves.\n
            	Serve hot Butter Chicken with naan, roti, or steamed rice.\n"""
            ch_image = "https://images.immediate.co.uk/production/volatile/sites/30/2021/02/butter-chicken-ac2ff98.jpg?quality=90&resize=440,400"  # replace with your image URL or local path
            st.image(ch_image, caption="Delicious Butter Chicken")

            st.markdown(butter_recipe)
            if st.button("Back to Dishes"):
                st.session_state['sub_page'] = 'punjab'
        elif st.session_state['sub_page'] == 'chole_recipe':
            st.subheader("Chole Recipe")

            chole_recipe =""" Instructions:\n
            For Chole:\n
                1.	Cook Chickpeas: Drain the soaked chickpeas. In a pressure cooker, add chickpeas, salt, and the tea bag. Add enough water to cover the chickpeas. Pressure cook for 6-7 whistles until they are soft. Discard the tea bag and set the cooked chickpeas aside.\n
                2.	Prepare the Masala: Heat oil in a pan. Add cumin seeds and let them splutter. Add chopped onions and sauté until golden brown. Add ginger-garlic paste and green chilies, and sauté for another 2 minutes.\n
                3.	Add Spices: Add turmeric powder, red chili powder, and coriander powder. Mix well and cook for 1 minute.\n
                4.	Add Tomatoes: Add tomato puree and cook until the oil separates from the masala.\n
                5.	Combine and Simmer: Add the cooked chickpeas to the masala. Mix well and add some of the cooking water from the chickpeas to achieve the desired consistency. Add garam masala and amchur powder. Simmer for 10-15 minutes, adjusting salt as needed.\n
                6.	Garnish: Garnish with fresh coriander leaves before serving.\n
            For Bhature:\n
                1.	Prepare the Dough: In a large bowl, mix flour, semolina, sugar, salt, and baking powder. Add yogurt and mix well. Gradually add water to make a soft dough. Knead the dough for 5-7 minutes until smooth.\n
                2.	Rest the Dough: Cover the dough with a damp cloth and let it rest for 2 hours.\n
                3.	Shape and Fry: Divide the dough into small balls. Roll each ball into a round or oval shape, about 1/4 inch thick. Heat oil in a deep frying pan. Deep fry the rolled dough until puffed and golden brown on both sides. Remove and drain on paper towels.\n
                4.	Serve: Serve the hot bhature with the prepared chole. Enjoy your delicious Chole Bhature!\n"""
            chole_image = "https://www.ekunji.com/wp-content/uploads/2015/09/chole-bhature-recipe.jpg"  # replace with your image URL or local path
            st.image(chole_image, caption="Delicious Chole Bature")

            st.markdown(chole_recipe)
            if st.button("Back to Dishes"):
                st.session_state['sub_page'] = 'punjab'
                st.experimental_rerun() 
        elif st.session_state['sub_page'] == 'rajasthan':
            st.subheader("Famous Dishes from Rajasthan")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Dal bati churma"):
                    st.session_state['sub_page'] = 'dal_recipe'
                    st.experimental_rerun()
                st.markdown('<div class="box dal">Dal bati churma</div>', unsafe_allow_html=True)
                if st.button("Kachori"):
                    st.session_state['sub_page'] = 'kachori_recipe'
                    st.experimental_rerun()
                st.markdown('<div class="box kachori">Kachori</div>', unsafe_allow_html=True)
                if st.button("Back"):
                    st.session_state['sub_page'] = 'north_indian'
                    st.experimental_rerun()
        elif st.session_state['sub_page'] == 'dal_recipe':
            st.subheader("Dal bati churma Recipe")

            dal_recipe = """Instructions:\n
            For Dal:\n
            1.	Cook the Lentils: Wash and soak the dals for 30 minutes. Drain and cook the dals in a pressure cooker with enough water, turmeric powder, and salt for 4-5 whistles or until soft. Mash slightly and set aside.\n
            2.	Prepare the Tempering: Heat ghee in a pan. Add cumin seeds, mustard seeds, and asafoetida. When they splutter, add onions and sauté until golden brown. Add ginger-garlic paste and green chilies, and sauté for another 2 minutes.\n
            3.	Add Tomatoes and Spices: Add tomatoes and cook until the oil separates from the masala. Add red chili powder, coriander powder, and garam masala. Mix well.\n
            4.	Combine and Simmer: Add the cooked dal to the pan. Adjust the consistency with water if needed. Simmer for 10-15 minutes, adjusting salt as needed.\n
            5.	Garnish: Garnish with fresh coriander leaves and serve hot.\n
            For Bati:\n
            1.	Prepare the Dough: In a large bowl, mix whole wheat flour, semolina, carom seeds, baking powder, and salt. Add ghee and mix until the mixture resembles breadcrumbs. Gradually add warm water to make a stiff dough. Knead well.\n
            2.	Shape and Bake: Preheat your oven to 180°C (350°F). Divide the dough into equal portions and shape them into round balls. Flatten slightly. Arrange the batis on a baking tray and bake for 30-35 minutes or until golden brown, flipping halfway.\n
            3.	Dip in Ghee: Once baked, dip the hot batis in melted ghee. Remove and set aside.\n
            For Churma:\n
            1.	Crumble the Bati: Crumble the batis into fine pieces using your hands or a food processor.\n
            2.	Toast with Ghee: Heat ghee in a pan. Add the crumbled bati and sauté until it turns golden brown.\n
            3.	Sweeten and Flavor: Remove from heat and mix in powdered jaggery or sugar and cardamom powder. Mix well. Garnish with chopped nuts if desired.\n
            4.	Serve: Serve the churma alongside the dal and bati.\n """
            dal_image = "https://vaya.in/recipes/wp-content/uploads/2018/04/dal-bati-churma.jpg"  # replace with your image URL or local path
            st.image(dal_image, caption="Delicious Dal Bati Churma")

            st.markdown(dal_recipe)
            if st.button("Back to Dishes"):
                st.session_state['sub_page'] = 'rajasthan'
                st.experimental_rerun()
        elif st.session_state['sub_page'] == 'kachori_recipe':
            st.subheader("Kachori Recipe")

            kachori_recipe="""Instructions:\n
            1.	Preparing the Dough:\n
        	In a large bowl, combine the all-purpose flour, ghee or oil, and salt. Mix well until the mixture resembles breadcrumbs.\n
        	Gradually add water and knead into a soft and smooth dough. Cover with a damp cloth and let it rest for 30 minutes.\n
            2.	Preparing the Filling:\n
        	Grind the soaked and drained moong dal coarsely in a blender or food processor without adding water.\n
        	Heat 2 tbsp oil in a pan over medium heat. Add cumin seeds, fennel seeds, and asafoetida. Sauté for a few seconds.\n
        	Add the ground moong dal and sauté for 5-6 minutes until it starts to dry out.\n
        	Add coriander powder, cumin powder, red chili powder, garam masala, dry mango powder, and salt. Mix well and cook for another 3-4 minutes.\n
        	Add gram flour and cook for another 2-3 minutes, stirring continuously to prevent lumps.\n
        	Add 2-3 tbsp water to the mixture and cook until the filling becomes dry and crumbly. Remove from heat and let it cool.\n
            3.	Assembling the Kachoris:\n
        	Divide the dough into small lemon-sized balls.\n
        	Roll out each ball into a small circle, about 3-4 inches in diameter.\n
        	Place a spoonful of the filling in the center of the rolled-out dough.\n
        	Gather the edges of the dough and seal the filling inside, pinching off any excess dough at the top.\n
        	Gently flatten the filled dough ball with your palms, being careful not to puncture the dough. Repeat with the remaining dough and filling.\n
            4.	Frying the Kachoris:\n
        	Heat oil in a deep frying pan over medium heat.\n
        	Once the oil is hot, reduce the heat to low-medium and gently slide in the prepared kachoris, a few at a time.\n
        	Fry the kachoris, turning occasionally, until they turn golden brown and crispy on all sides. This should take about 6-8 minutes per batch.\n
        	Remove the fried kachoris with a slotted spoon and drain on paper towels.\n
            5.	Serving:\n
        	Serve hot kachoris with tamarind chutney, green chutney, or a side of yogurt.\n """
            kachori_image = "https://manjulaskitchen.com/wp-content/uploads/khasta_khachori.jpg"  # replace with your image URL or local path
            st.image(kachori_image, caption="Delicious Kachori")

            st.markdown(kachori_recipe)
            if st.button("Back to Dishes"):
                st.session_state['sub_page'] = 'rajasthan'
                st.experimental_rerun()        
        elif st.session_state['sub_page'] == 'kerala':
            st.subheader("Famous Dishes from Kerala")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Puttu"):
                    st.session_state['sub_page'] = 'puttu_recipe'
                    st.experimental_rerun()
                st.markdown('<div class="box puttu">Puttu</div>', unsafe_allow_html=True)
                if st.button("Thalassery Biryani"):
                    st.session_state['sub_page'] = 'thalassery_recipe'
                    st.experimental_rerun()
                st.markdown('<div class="box thalassery">Thalassery Biryani</div>', unsafe_allow_html=True)
                if st.button("Back"):
                    st.session_state['sub_page'] = 'south_indian'
                    st.experimental_rerun()
            
        elif st.session_state['sub_page'] == 'puttu_recipe':
            st.subheader("Puttu Recipe")

            puttu_recipe = """  
            Instructions:\n
                1.	Prepare the Puttu Flour Mixture:\n
                	In a mixing bowl, combine the rice flour and salt.\n
                	Slowly add water little by little, mixing with your fingers or a spoon until the mixture resembles coarse breadcrumbs. The texture should be crumbly and moist but not wet.\n
                2.	Prepare the Puttu Vessel:\n
                  	Traditionally, a Puttu kutti or a cylindrical steamer is used. If you don't have one, you can use a steamer basket lined with a cloth or a regular idli steamer plate.
                3.	Layering and Steaming:\n
                	Line the steamer basket or idli plates with a thin cloth.\n
                	Add a layer of grated coconut (if using) followed by a layer of the rice flour mixture.\n
                	Steam for 8-10 minutes until cooked.\n
                4.	Serving:\n
                	Once cooked, gently push the puttu out from the cylindrical container or remove from the steamer.\n
                	Serve hot with kadala curry (black chickpea curry), banana, or sugar and ghee. Puttu also pairs well with a variety of curries and side dishes.\n"""
            puttu_image = "https://www.holidify.com/blog/wp-content/uploads/2015/11/5645919324_30efcbe343_z.jpg"  # replace with your image URL or local path
            st.image(puttu_image, caption="Delicious puttu")
            

            st.markdown(puttu_recipe)
            if st.button("Back to Dishes"):
                st.session_state['sub_page'] = 'kerala'
                st.experimental_rerun()
        elif st.session_state['sub_page'] == 'thalassery_recipe':
            st.subheader("Thalassery biriyani recipe")

            thalassery_recipe = """
            Instructions:\n
                1.	Marinating the Chicken:\n
                	In a bowl, mix together t0he chicken pieces with yogurt, ginger-garlic paste, turmeric powder, red chili powder, biriyani masala powder, and salt. Marinate for at least 30 minutes (preferably 2 hours) in the refrigerator.\n
                2.	Cooking the Rice:\n
                	In a large pot, bring 4 cups of water to a boil.\n
                	Add cloves, green cardamom pods, cinnamon stick, bay leaf, and salt.\n
                	Add soaked and drained basmati rice. Cook until the rice is 70-80 percent done (parboiled). Drain and set aside.\n
                3.	Preparing the Biriyani Masala:\n
                	Grind all the ingredients listed under "Biriyani Masala" into a smooth paste using a little water if necessary.\n
                4.	Cooking the Chicken Masala:\n
                	Heat ghee and oil in a large heavy-bottomed pot or biriyani pot.\n
                	Add thinly sliced onions and sauté until golden brown.\n
                	Add chopped tomatoes and cook until they turn soft.\n
                	Add the ground biriyani masala paste and sauté for 5-6 minutes until the raw smell disappears and the masala is cooked well.\n
                5.	Layering and Dum Cooking:\n
                	Reduce the heat to low. Layer half of the parboiled rice over the chicken masala.\n
                	Sprinkle half of the fried onions, fresh cilantro leaves, and optionally, cashews and raisins.\n
                	Layer the remaining rice over this and top with the remaining fried onions, cilantro leaves, and optionally, cashews and raisins.\n
                	Drizzle saffron soaked in warm milk over the top (if using).\n
                6.	Dum Cooking (Steaming):\n
                	Cover the pot with a tight-fitting lid. You can seal the edges with dough or a clean cloth to trap the steam.\n
                	Cook on very low heat (dum) for 20-25 minutes until the rice and chicken are fully cooked and infused with flavors.\n
                7.	Serve:\n
                	Once done, gently mix the biriyani from the edges to combine the layers.\n
                	Serve hot Thalassery Biriyani with raita, pickle, and salad.\n"""
            thalaserry_image = "https://farm5.staticflickr.com/4206/34630446624_ec6133ed16_o_d.jpg"  # replace with your image URL or local path
            st.image(thalaserry_image, caption="Delicious thalaserry biriyani")

            st.markdown(thalassery_recipe)
            if st.button("Back to Dishes"):
                st.session_state['sub_page'] = 'kerala'
                st.experimental_rerun()
        elif st.session_state['sub_page'] == 'andhra':
            st.subheader("Famous Dishes from Andhra Pradesh")

            col1, col2 = st.columns(2)
            with col1:
                if st.button("Gutti Vankaya Kura"):
                    st.session_state['sub_page'] = 'gutti_recipe'
                    st.experimental_rerun()
                st.markdown('<div class="box gutti">Gutti Vankaya Kura</div>', unsafe_allow_html=True)
                if st.button("Hyderabadi Biryani"):
                    st.session_state['sub_page'] = 'biriyani_recipe'
                    st.experimental_rerun()
                st.markdown('<div class="box biriyani">Hyderabadi Biryani</div>', unsafe_allow_html=True)
                if st.button("Back"):
                    st.session_state['sub_page'] = 'south_indian'
                    st.experimental_rerun()
            
        elif st.session_state['sub_page'] == 'gutti_recipe':
            st.subheader("Gutti Recipe")

            gutti_recipe = """ Instructions: \n
            1.	Preparing the Brinjals:\n
                Wash and dry the brinjals. Make a plus-shaped incision at the base of each brinjal, ensuring the stems remain intact. Keep them immersed in water to prevent discoloration.\n
            2.	Making the Stuffing:\n
                In a bowl, mix together roasted peanuts, roasted sesame seeds, roasted desiccated coconut, tamarind pulp, jaggery or sugar, red chili powder, coriander powder, cumin powder, and salt. Adjust seasoning to taste.\n
            3.	Stuffing the Brinjals:\n
                Gently stuff each brinjal with the prepared stuffing mixture using a spoon or your fingers. Press lightly to fill the cavity without breaking the brinjal.\n
            4.	Cooking the Curry:\n
                Heat oil in a wide pan or kadai over medium heat.\n
                Add mustard seeds and let them splutter. Add cumin seeds, asafoetida, and curry leaves. Saute for a few seconds.\n
                Add finely chopped onions and saute until they turn golden brown.\n
                Add ginger-garlic paste and saute until the raw smell disappears.\n
                Add finely chopped tomatoes, turmeric powder, and salt. Cook until tomatoes turn soft and oil begins to separate from the mixture.\n
            5.	Cooking the Stuffed Brinjals:\n
                Carefully arrange the stuffed brinjals in the pan, ensuring they are in a single layer.\n
                Add any remaining stuffing mixture over the brinjals.\n
                Add about 1/2 cup of water, cover with a lid, and simmer on low heat for 20-25 minutes or until the brinjals are cooked through and tender. Occasionally, gently stir the brinjals without breaking them.\n
            6.	Finishing Touches:\n
                Once the brinjals are cooked and the curry has thickened, garnish with fresh cilantro leaves.\n
                Serve hot Gutti Vankaya Kura with steamed rice or roti.\n """
            gutti_image = "https://blog.swiggy.com/wp-content/uploads/2024/03/Gutti-Vankaya-Kura.png"  # replace with your image URL or local path
            st.image(gutti_image, caption="Delicious Gutti Vankaya Kura")
            st.markdown(gutti_recipe)
            if st.button("Back to Dishes"):
                st.session_state['sub_page'] = 'andhra'
                st.experimental_rerun()
        elif st.session_state['sub_page'] == 'biriyani_recipe':
            st.subheader("Hyderabadi Biriyani Recipe")

            biriyani_recipe = """ Instructions:\n
            1.	Marinating the Chicken:\n
            	In a bowl, mix together chicken pieces, yogurt, ginger-garlic paste, red chili powder, turmeric powder, biryani masala powder, and salt. Marinate for at least 2 hours in the refrigerator.\n
            2.	Cooking the Rice:\n
            	In a large pot, bring 6 cups of water to a boil.\n
            	Add cloves, green cardamom pods, cinnamon stick, bay leaf, and salt.\n
            	Add soaked and drained basmati rice. Cook until the rice is 70-80% done (parboiled). Drain and set aside.\n
            3.	Frying Onions (Biryani Essence):\n
            	Heat oil in a deep pan or kadai over medium heat.\n
            	Add thinly sliced onions and fry until they turn golden brown and crispy. Remove and drain on paper towels.\n
            4.	Preparing the Biryani Masala:\n
            	Heat ghee and oil in a large heavy-bottomed pot or biryani pot over medium heat.\n
            	Add shahi jeera, bay leaves, green cardamom pods, cloves, and cinnamon stick. Saute for a minute until aromatic.\n
            5.	Cooking the Chicken Masala:\n
            	Add thinly sliced onions and sauté until they turn golden brown.\n
            	Add chopped tomatoes and cook until they turn soft.\n
            	Add marinated chicken pieces along with the marinade. Cook on medium-high heat for 5-7 minutes until the chicken is partially cooked and the masala thickens.\n
            	Add yogurt and mix well. Cook for another 5 minutes until the chicken is almost cooked through and the masala is well-coated.\n
            6.	Layering the Biryani:\n
            	Reduce the heat to low. Layer half of the parboiled rice over the chicken masala.\n
            	Sprinkle half of the fried onions, chopped fresh mint leaves, and chopped fresh cilantro leaves.\n
            	Drizzle with half of the melted ghee or butter.\n
            	Repeat the layers with the remaining rice, fried onions, mint leaves, cilantro leaves, and melted ghee or butter.\n
            	Optionally, drizzle saffron soaked in warm milk over the top for added color and flavor.\n
            7.	Dum Cooking (Steaming):\n
            	Cover the pot with a tight-fitting lid. You can seal the edges with dough or a clean cloth to trap the steam.\n
            	Cook on very low heat (dum) for 30-35 minutes until the rice is fully cooked and infused with flavors.\n
            8.	Serve:\n
            	Once done, gently mix the biryani from the edges to combine the layers.\n
            	Garnish with fresh cilantro leaves and fried onions.\n
            	Serve hot Hyderabadi Biryani with raita, salad, and pickle. """
            biriyani_image = "https://www.licious.in/blog/wp-content/uploads/2020/12/Hyderabadi-chicken-Biryani-600x600.jpg"  # replace with your image URL or local path
            st.image(biriyani_image, caption="Delicious Biryani")
            st.markdown(biriyani_recipe)
            if st.button("Back to Dishes"):
                st.session_state['sub_page'] = 'andhra'
                st.experimental_rerun()
        elif st.session_state['sub_page'] == 'karnataka':
            st.subheader("Famous Dishes from Karnataka")

            col1, col2 = st.columns(2)
            with col1:
                if st.button("Bisi Bele Bath"):
                    st.session_state['sub_page'] = 'bath_recipe'
                    st.experimental_rerun()
                st.markdown('<div class="box bath">Bisi Bele Bath</div>', unsafe_allow_html=True)
                if st.button("Mysore Masala Dosa"):
                    st.session_state['sub_page'] = 'dosa_recipe'
                    st.experimental_rerun()
                st.markdown('<div class="box dosa">Mysore Masala Dosa</div>', unsafe_allow_html=True)
                if st.button("Back"):
                    st.session_state['sub_page'] = 'south_indian'
                    st.experimental_rerun()
            
            
        elif st.session_state['sub_page'] == 'bath_recipe':
            st.subheader("Bisi Bele Bath Recipe")

            bath_recipe = """Instructions: \n
            1.	Prepare Bisi Bele Bath Powder (Spice Mix):\n
            	Heat 1 tbsp oil in a pan over medium heat.\n
            	Add all the ingredients listed under "Bisi Bele Bath Powder" except coconut and roast until fragrant and lightly browned.\n
            	Add grated coconut and roast until it turns golden brown.\n
            	Allow it to cool and then grind into a fine powder using a spice grinder or mixer. Set aside.\n
            2.	Cooking Rice and Dal:\n
            	Wash rice and toor dal separately and drain.\n
            	In a pressure cooker or large pot, cook rice and dal with 4 cups of water, turmeric powder, and a pinch of salt until soft and well-cooked. Mash lightly and set aside.\n
            3.	Preparing Bisi Bele Bath:\n
            	Heat ghee in a large pan or kadai over medium heat.\n
            	Add chopped onions and sauté until golden brown.\n
            	Add chopped tomatoes and cook until they turn soft and mushy.\n
            	Add mixed vegetables and sauté for a few minutes.\n
            4.	Adding Spice Mix and Tamarind Paste:\n
            	Add 3-4 tbsp of the prepared Bisi Bele Bath powder (adjust to taste) and mix well with the vegetables.\n
            	Pour the tamarind paste mixture (dissolved in water) into the pan.\n
            	Add salt and jaggery or sugar (if using). Mix well and cook for 5-7 minutes until the raw smell of the spices disappears and the vegetables are cooked through.\n
            5.	Combining Rice, Dal, and Masala:\n
            	Add the cooked rice and dal mixture to the pan with the masala.\n
            	Mix everything together gently, ensuring the rice and dal are well-coated with the masala. Adjust consistency by adding water if needed (Bisi Bele Bath should be slightly thick).\n
            6.	Tempering (Optional):\n
            	In a small pan, heat a little ghee.\n
            	Add a pinch of asafoetida (hing) and roasted peanuts. Fry until peanuts turn golden brown.\n
            	Pour this tempering over the Bisi Bele Bath and mix gently.\n
            7.	Serve:\n
            	Garnish with fresh cilantro leaves.\n
            	Serve hot Bisi Bele Bath with a side of papad, raita, or potato chips.\n"""
            bath_image = "https://www.vegrecipesofindia.com/wp-content/uploads/2018/10/bisi-bele-bath-recipe-1.jpg"  # replace with your image URL or local path
            st.image(bath_image, caption="Delicious Bisi Bele Bath")
            st.markdown(bath_recipe)
            if st.button("Back to Dishes"):
                st.session_state['sub_page'] = 'karnataka'
                st.experimental_rerun()
        elif st.session_state['sub_page'] == 'dosa_recipe':
            st.subheader("Mysore Masala Dosa Recipe")
            dosa_recipe = """ Instructions: \n
            1.	Preparing Dosa Batter:\n
            	Wash and soak rice, urad dal, chana dal, and poha in separate bowls with enough water for 4-6 hours or overnight.\n
            	Drain the water and grind everything together into a smooth batter using a wet grinder or a high-speed blender. Add water as needed to achieve a thick pouring consistency.\n
            	Add salt to taste and mix well. Allow the batter to ferment in a warm place for 8-12 hours or until it doubles in volume.\n
            2.	Making Mysore Masala Dosa Chutney:\n
            	In a blender, combine grated coconut, roasted chana dal, dry red chilies, ginger, garlic, tamarind paste, and salt.\n
            	Add water gradually and blend into a smooth paste. Adjust consistency as needed. Set aside.\n
            3.	Preparing Potato Masala (Filling):\n
            	Heat oil in a pan over medium heat.\n
            	Add mustard seeds and let them splutter. Add cumin seeds, asafoetida, and curry leaves. Saute for a few seconds.\n
            	Add chopped onions and green chilies. Saute until onions turn golden brown.\n
            	Add turmeric powder and sauté for a few seconds.\n
            	Add mashed potatoes and salt. Mix well and cook for 2-3 minutes until flavors blend together.\n
                Garnish with fresh cilantro leaves. Keep aside.\n
            4.	Making Mysore Masala Dosa:\n
            	Heat a dosa tawa or non-stick skillet over medium-high heat. Once hot, lower the heat slightly.\n
            	Pour a ladleful of dosa batter onto the center of the tawa and spread it in a circular motion to make a thin dosa.\n
            	Drizzle a teaspoon of ghee or oil around the edges of the dosa.\n
            	Spread a generous amount of Mysore masala dosa chutney evenly all over the dosa surface.\n
            	Place a portion of potato masala filling on one side of the dosa.\n
            	Optionally, add a dollop of butter on top of the potato masala for added richness.\n
            	Cook the dosa until the edges start to lift off the tawa and the underside turns golden brown and crisp.\n
            	Fold the dosa in half or roll it and transfer to a serving plate.\n
            5.	Serving:
            	Serve hot Mysore Masala Dosa with coconut chutney and sambar.\n"""
            dosa_image = "https://www.awesomecuisine.com/wp-content/uploads/2014/07/mysore_masala_dosa.jpg"  # replace with your image URL or local path
            st.image(dosa_image, caption="Mysore Masala Dosa")
            st.markdown(dosa_recipe)
            if st.button("Back to Dishes"):
                st.session_state['sub_page'] = 'karnataka'
                st.experimental_rerun()
        elif st.session_state['sub_page'] == 'tamilnadu':
            st.subheader("Famous Dishes from Tamil Nadu")

            col1, col2 = st.columns(2)
            with col1:
                if st.button("Sambar"):
                    st.session_state['sub_page'] = 'sambar_recipe'
                    st.experimental_rerun()
                st.markdown('<div class="box sambar">Sambar</div>', unsafe_allow_html=True)
                if st.button("Pongal"):
                    st.session_state['sub_page'] = 'pongal_recipe'
                    st.experimental_rerun()
                st.markdown('<div class="box pongal">Pongal</div>', unsafe_allow_html=True)
                if st.button("Back"):
                    st.session_state['sub_page'] = 'south_indian'
                    st.experimental_rerun()
                

        elif st.session_state['sub_page'] == 'sambar_recipe':
            st.subheader("Sambar Recipe")

            sambar_recipe = """
            \nInstructions:\n
            1.	Cooking the Toor Dal:\n
        	    Rinse the toor dal under water until it runs clear.\n
        	    In a pressure cooker or a pot, cook the toor dal with 1.5 cups of water, turmeric powder, and a pinch of salt until it is soft and mushy (about 3-4 whistles in a pressure cooker or simmer for 20-25 minutes in a pot).\n
        	    Mash the dal well and set aside.\n
            2.	Preparing the Sambar Powder (if making from scratch):\n
        	    Dry roast all the ingredients listed under "Sambar Powder" until they turn aromatic and golden brown.\n
        	    Cool and grind into a fine powder.\n
            3.	Making the Tiffin Sambar:\n
        	    Heat oil in a pan or kadai over medium heat. Add mustard seeds and let them splutter.\n
        	    Add cumin seeds, dry red chilies, and curry leaves. Sauté for a few seconds until fragrant.\n
        	    Add chopped onions and sauté until they turn translucent.\n
        	    Add mixed vegetables and sauté for 2-3 minutes.\n
            4.	Cooking the Sambar:\n
            	Add chopped tomatoes and cook until they turn soft.\n
            	Add sambar powder (if using store-bought) or the homemade sambar powder. Sauté for a minute.\n
            	Add the cooked and mashed toor dal along with 1.5 cups of water (adjust consistency as needed).\n
            	Add diluted tamarind paste and salt to taste. Mix well.\n
            5.	Simmering the Sambar:\n
            	Let the sambar simmer on low heat for 10-15 minutes, allowing the flavors to blend together and the vegetables to cook through.\n
            	Adjust seasoning and consistency if needed by adding more water.\n
            6.	Finishing Touches:\n
            	Garnish with fresh coriander leaves.\n
            	Serve hot with idli, dosa, vada, or any tiffin item of your choice.\n
            7.	That's it, sambar is ready!\n


            """
            sambar_image = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Pumpkin_sambar.JPG/800px-Pumpkin_sambar.JPG"  # replace with your image URL or local path
            st.image(sambar_image, caption="Delicious Sambar")
            

            st.markdown(sambar_recipe)

            if st.button("Back to Dishes"):
                st.session_state['sub_page'] = 'tamilnadu'
                st.experimental_rerun()

        elif st.session_state['sub_page'] == 'pongal_recipe':
            st.subheader("Pongal Recipe")

            pongal_recipe = """Instructions: \n
            1.	Preparation:\n
            	Wash the rice and moong dal together until the water runs clear.\n
            	In a pressure cooker, add the washed rice and moong dal, turmeric powder, and 3 cups of water.\n
            	Pressure cook for 3-4 whistles or until both the rice and dal are cooked soft and mushy.\n
            2.	Tempering:\n
            	In a small pan, heat the ghee.\n
            	Add the black peppercorns and cumin seeds. Let them splutter.\n
            	Add the grated ginger and sauté for a few seconds.\n
            	Add the cashew nuts and fry until golden brown.\n
            	Add a pinch of asafoetida and the curry leaves. Sauté for a few seconds until the leaves turn crispy.\n
            3.	Combining:\n
            	Open the pressure cooker once the pressure releases naturally.\n
            	Add salt to taste and mix well.\n
            	Pour the tempering mixture over the cooked rice and dal. Mix thoroughly.\n
            4.	Serving:\n
            	Serve hot with a side of coconut chutney or sambar. If you want the recipe for sambar, you can check it on our page.\n

            """
            pongal_image = "https://www.vegrecipesofindia.com/wp-content/uploads/2019/01/ven-pongal-recipe-1a.jpg"  # replace with your image URL or local path
            st.image(pongal_image, caption="Delicious Pongal")
            st.markdown(pongal_recipe)

            if st.button("Back to Dishes"):
                st.session_state['sub_page'] = 'tamilnadu'
                st.experimental_rerun()


if st.session_state['logged_in']:
    main_page()
else:
    
    st.title("Login or Register")
    login_or_register = st.radio("Select an option", ("Login", "Register"))
    
    if login_or_register == "Login":
        login()
    elif login_or_register == "Register":
        register()