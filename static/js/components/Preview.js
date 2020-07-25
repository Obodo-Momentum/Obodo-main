import React from 'react'
import Card from 'react-bootstrap/Card'

export default function Preview ({ title, post_text, category, request_or_offer, location, timeline_start, timeline_end, post_image, tag_names }) {
  const imageUrl = {
    kids: 'https://images.pexels.com/photos/1148998/pexels-photo-1148998.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
    outdoors: 'https://images.pexels.com/photos/169523/pexels-photo-169523.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500',
    services: 'https://images.pexels.com/photos/339620/pexels-photo-339620.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500',
    food: 'https://images.pexels.com/photos/3621212/pexels-photo-3621212.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500',
    clothing: 'https://images.pexels.com/photos/996329/pexels-photo-996329.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500',
    homegoods: 'https://images.pexels.com/photos/1528975/pexels-photo-1528975.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500',
    furniture: 'https://images.pexels.com/photos/1248583/pexels-photo-1248583.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500',
    books: 'https://images.pexels.com/photos/279222/pexels-photo-279222.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500'
  }

  return (
    <div>
      <Card style={{ width: '18rem' }}>
        <Card.Img variant='top' src={post_image} />
        <Card.Body>
          <Card.Title>{title}</Card.Title>
          <Card.Subtitle>{request_or_offer}</Card.Subtitle>
          <Card.Subtitle>{category}</Card.Subtitle>
          <Card.Text>
            {post_text}
          </Card.Text>
          <footer>
            <div>{timeline_start} - {timeline_end}</div>
            <div>{category}</div>
            <div>{tag_names}</div>
          </footer>
        </Card.Body>
      </Card>
    </div>)
}
