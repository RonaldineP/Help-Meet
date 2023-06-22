import React, { useEffect, useContext } from 'react';
import { Context } from "../store/appContext";
import Paymentmodal from "../component/paymentmodal"
import PayPal from '../component/paypal';
import "../../styles/post.css"

export const Post = () => {
  const { store, actions } = useContext(Context);

  useEffect(() => {
    // Fetch user posts and post candidates when the component mounts
    actions.fetchUserPosts();
  }, []);

  const { posts, user } = store;

  // Render the userPosts and associated postCandidates
  return (
    <div className='post-container'>
      <h1>User Posts</h1>
      {posts.filter((item, index) => item.user_id == user.id).map((post, index) => {
        return (
          <div className="post-body">
            <div className="user-info">
              <div className='d-flex w-100'>
                <div className='w-50'>
                  <img src={post.user.profile_image} alt="User Profile Image" className="user-profile-image me-auto" />
                </div>
                <div className='w-50'>
                  <p>{post.user.name}</p>
                </div>
              </div>
              <p className="post-text">{post.description}</p>
              <div className="post-images">
                {post.images.map((image) => (
                  <div className="image-wrapper" key={image.id}>
                    <img src={image.url} alt="Post Image" />
                  </div>
                ))}
              </div>
            </div>
            <div className="post-info">
              <p className="timestamp">{post.timestamp}</p>
              <p className="location">
                {post.city}, {post.location}
              </p>
            </div>
            <div className="post-candidates">

              <h3>Post Candidates</h3>
              <ul>
                {post.post_candidates
                  .filter((candidate) => candidate.postid === post.id)
                  .map((candidate) => (
                    <li key={candidate.id}>
                      <div className="candidate-info">

                        <img src={candidate.profile_image} alt="Candidate Profile Image" className="profile_image" />
                        <p>{candidate.name}</p>
                      </div>

                    </li>
                  ))}
              </ul>
              <div className="form-check form-switch">
                <input className="form-check-input" type="checkbox" id="flexSwitchCheckDefault" />
                <label className="form-check-label" type="flexSwitchCheckDefault"></label>
              </div>
            </div>
            <Paymentmodal></Paymentmodal>
          </div>
        )
      })}

    </div>
  );
};