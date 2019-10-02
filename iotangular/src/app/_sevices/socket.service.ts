import { Injectable } from '@angular/core';
import * as io from 'socket.io-client';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SocketService {
  private socket: SocketIOClient.Socket;
  private messages: Array<any>;
  constructor() {
    //this.connect();
   // this.getMessage();
  }

  public connect(){
    this.socket = io('http://localhost:5000'); 
  }
  public sendMessage(message: any) {
    this.socket.emit('new-message', message);
  }

  public getMessage(){
    this.socket.on('data-tmp', (data) => {
      console.log(data);
    });
  }

}

