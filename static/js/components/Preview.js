import React from 'react'
import Card from 'react-bootstrap/Card'

export default function Preview ({ title, post_text, category, request_or_offer, location, timeline_start, timeline_end, post_image, tag_names  }) {
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
