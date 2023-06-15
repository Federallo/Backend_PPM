# **Backend_PPM**
back-end excercise for ppm:
## **Topic**
**Music streaming service**:<br />
**Models**: Define models for songs, playlists, user profiles, and recommendations. Establish relationships to organize music content and user preferences.<br />
**Views**: Create views for song listings, playlist creation, user profiles, and recommendation algorithms.
Implement search and filtering functionalities.<br />
**Templates**: Design templates for song listings, playlist creation, user profiles, and personalized recommendations. Include features for playlist sharing.<br />
**Forms**: Develop forms for playlist creation, user registration, and login.<br />
**Authentication**: Implement user authentication to enable playlist creation, track user preferences, and provide personalized music recommendations.
### **Models**
- CustomUser (using django built-in features)
- Songs 
- Playlist
- Recommnendation
- SongSerializer (to filter songs using rest_framework)

### **Views**
- User customization (login, change password, sign up | using django built-in features).
- Playlist customization (create, edit, add songs, remove songs, delete, share (only for logged users) | using django built-in features).
- Playlist sharing by generating a url, using HttpResponse, which every user can open.
- Song index, with filtering functionalities (which also features search).
- Recommendations based on user's playlists: the algorithm keeps tracking users' genres inside their playlists, chooses which genres appears the most, and gives a list of 10 recommended songs.

## **Extras**
I've created two profiles:
- username: test | password: nkiGdxHKns7SyC7
  - this profile has a playlists created with recommendations
- username: test2 | password: 4BSG8Dp6YkPM54H
  - this profile was created for testing playlist sharing
