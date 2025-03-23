import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, RouterModule } from '@angular/router';
import { AlbumsService } from '../albums.service';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-album-photos',
  standalone: true,
  imports:[CommonModule, RouterModule],
  templateUrl: './album-photos.component.html',
  styleUrls: ['./album-photos.component.css']
})
export class AlbumPhotosComponent implements OnInit {
  photos: any[] = [];

  constructor(private route: ActivatedRoute, private http: HttpClient) {}

  ngOnInit() {
    const id = this.route.snapshot.paramMap.get('id');
    if (id) {
      this.http.get<any[]>(`https://jsonplaceholder.typicode.com/albums/${id}/photos`)
        .subscribe(data => {
          this.photos = data;
        });
    }
  }
}
