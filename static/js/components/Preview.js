import React from 'react'
import Card from 'react-bootstrap/Card'
import { propTypes } from 'react-bootstrap/esm/Image'

export default function Preview ({ title, post_text, category, request_or_offer, location, timeline_start, timeline_end, post_image, tag_names }) {
  let imageUrl = ''
  switch (category) {
    case 'kids':
      imageUrl = 'https://images.pexels.com/photos/1148998/pexels-photo-1148998.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260'
      break
    case 'outdoors':
      imageUrl = 'https://images.pexels.com/photos/169523/pexels-photo-169523.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500'
      break
    case 'services':
      imageUrl = 'https://images.pexels.com/photos/339620/pexels-photo-339620.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500'
      break
    case 'food':
      imageUrl = 'https://images.pexels.com/photos/3621212/pexels-photo-3621212.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500'
      break
    case 'clothing':
      imageUrl = 'https://images.pexels.com/photos/996329/pexels-photo-996329.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500'
      break
    case 'homegoods':
      imageUrl = 'https://images.pexels.com/photos/1528975/pexels-photo-1528975.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500'
      break
    case 'furniture':
      imageUrl = 'https://images.pexels.com/photos/1248583/pexels-photo-1248583.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500'
      break
    case 'books':
      imageUrl = 'https://images.pexels.com/photos/279222/pexels-photo-279222.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500'
      break
    default:
      imageUrl = 'https://images.pexels.com/photos/45842/clasped-hands-comfort-hands-people-45842.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500'
  }
  return (
    <div>
      <Card style={{ width: '18rem' }}>
        <Card.Img variant='top' src={imageUrl} />
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
