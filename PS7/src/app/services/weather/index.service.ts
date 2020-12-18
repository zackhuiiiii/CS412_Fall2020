import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class IndexService {

  constructor(private client: HttpClient) { }

  query(city_name: string) {
    return this.client.post('/ps4/weather', {city_name})
    // .subscribe(data=>{
    // .pipe(data=>{
    //   console.log(data)
    // });
  }
}
